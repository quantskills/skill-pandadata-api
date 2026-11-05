#!/usr/bin/env python3
"""Generate an SDK contract from an explicitly selected, checksum-verified release."""
import argparse
import ast
import hashlib
import io
from importlib.metadata import version
import inspect
import json
from pathlib import Path
import re
import textwrap
import urllib.request
import zipfile


def describe_method(name,function):
    signature=inspect.signature(function)
    parameters={key:param for key,param in signature.parameters.items()
                if param.kind not in (param.VAR_POSITIONAL,param.VAR_KEYWORD)}
    required=set()
    for node in ast.walk(ast.parse(textwrap.dedent(inspect.getsource(function)))):
        if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id=='validate_not_empty':
            if node.args and isinstance(node.args[0],ast.Name):required.add(node.args[0].id)
            if len(node.args)>1 and isinstance(node.args[1],ast.Constant):required.add(node.args[1].value)
    # SDK auth defaults can be populated from private environment/configuration.
    display="(username=..., password=..., base_url=..., country='CN')" if name=='init_token' else str(signature)
    return {'signature':display,'parameters':list(parameters),
            'required':[key for key,param in parameters.items() if param.default is param.empty],
            'runtime_required':sorted(required & set(parameters)),
            'upstream_warning':'WARNING' in (inspect.getdoc(function) or '')}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version',required=True,help='Explicit stable SDK version; install it first.')
    parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parents[1]/'references/sdk-contract.json')
    args=parser.parse_args()
    if not re.fullmatch(r'\d+\.\d+\.\d+',args.version):parser.error('Select an explicit stable three-part version.')
    if version('panda-data')!=args.version:parser.error('Installed distribution does not match the selected version.')
    metadata=json.load(urllib.request.urlopen(f'https://pypi.org/pypi/panda-data/{args.version}/json'))
    wheel=next(w for w in metadata['urls'] if w['filename']==f'panda_data-{args.version}-py3-none-any.whl')
    archive=urllib.request.urlopen(wheel['url']).read()
    if hashlib.sha256(archive).hexdigest()!=wheel['digests']['sha256']:
        raise RuntimeError('Published wheel checksum verification failed')
    import panda_data
    package=Path(panda_data.__file__).resolve().parent
    with zipfile.ZipFile(io.BytesIO(archive)) as published:
        for name in published.namelist():
            if name.startswith('panda_data/') and name.endswith('.py'):
                installed=package/Path(name).relative_to('panda_data')
                if not installed.is_file() or installed.read_bytes()!=published.read(name):
                    raise RuntimeError('Installed Python sources differ from the verified wheel')
    methods={name:describe_method(name,getattr(panda_data,name)) for name in dir(panda_data)
             if (name.startswith('get_') or name=='init_token') and callable(getattr(panda_data,name))}
    validation={'offline_contract':'not_tested','live_service':'not_tested'}
    if args.output.exists():
        previous=json.loads(args.output.read_text(encoding='utf-8'))
        if previous.get('sdk_version')==args.version and previous.get('wheel_sha256')==wheel['digests']['sha256']:
            validation=previous.get('validation',validation)
    result={'schema_version':1,'sdk_version':args.version,'distribution':'panda-data',
            'requires_python':metadata['info']['requires_python'],'wheel_url':wheel['url'],
            'wheel_sha256':wheel['digests']['sha256'],'source':f'https://pypi.org/project/panda-data/{args.version}/',
            'maintainer':'abgyjaguo','validation':validation,'methods':methods}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Wrote {len(methods)} callable contracts for panda_data {args.version}; credentials are never serialized.')
    return 0


if __name__=='__main__':raise SystemExit(main())
