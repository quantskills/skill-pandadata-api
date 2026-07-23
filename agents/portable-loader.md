# Portable Loader Prompt

Use this prompt in agents that do not natively discover `SKILL.md` folders.

```text
You have access to a local skill named pandadata-api at:
<PANDADATA_SKILL_ROOT>

When the user asks about Pandadata, panda_data, Pandadata API methods, request parameters, response fields, or Python examples:
1. Read <PANDADATA_SKILL_ROOT>/SKILL.md.
2. Select an interpreter with panda_data==0.0.12; prefer PANDADATA_PYTHON or the skill's virtual environment. The runtime scripts reject other SDK versions.
3. Read <PANDADATA_SKILL_ROOT>/references/sdk-0.0.12.md, then consult <PANDADATA_SKILL_ROOT>/references/method-index.md.
4. For exact method details, run:
   <PANDADATA_PYTHON> <PANDADATA_SKILL_ROOT>/scripts/search_api_docs.py --method <method>
5. For real API calls, prefer:
   <PANDADATA_PYTHON> <PANDADATA_SKILL_ROOT>/scripts/call_api.py --method <method> --params '<json>'
   It checks credentials and runs setup when needed.
6. Use the exact documented parameters and examples from <PANDADATA_SKILL_ROOT>/references/api-docs.md.
7. Do not generate Python SDK calls for methods marked `not exported` by panda_data 0.0.12.
8. Do not invent SDK installation, token, login, field names, or undocumented API behavior.
```
