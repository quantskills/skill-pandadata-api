# Portable Loader Prompt

Use this prompt in agents that do not natively discover `SKILL.md` folders.

```text
You have access to a local skill named pandadata-api at:
<PANDADATA_SKILL_ROOT>

When the user asks about Pandadata, panda_data, Pandadata API methods, request parameters, response fields, or Python examples:
1. Read <PANDADATA_SKILL_ROOT>/SKILL.md.
2. Consult <PANDADATA_SKILL_ROOT>/references/method-index.md first.
3. For exact method details, run:
   python <PANDADATA_SKILL_ROOT>/scripts/search_api_docs.py --method <method>
4. For real API calls, prefer:
   python <PANDADATA_SKILL_ROOT>/scripts/call_api.py --method <method> --params '<json>'
   It checks credentials and runs setup when needed.
5. Use the exact documented parameters and examples from <PANDADATA_SKILL_ROOT>/references/api-docs.md.
6. Do not invent SDK installation, token, login, field names, or undocumented API behavior.
```
