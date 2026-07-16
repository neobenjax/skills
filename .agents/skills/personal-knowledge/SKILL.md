---
name: personal-knowledge
description: "Use this skill to answer personal questions about the user such as 'who am I', 'where do I live', 'what is my experience', etc."
---

# Personal Knowledge Skill Instructions

When the user asks you a personal question about themselves (e.g. "who am I", "what is my name", "where do I work"), you MUST follow this exact procedure:

1. **Query Local Knowledge**: Use your `view_file` or `grep_search` tools to read the Open Knowledge Format (OKF) files located in the `knowledge-catalog/` directory (relative to the workspace root). Specifically, look at `knowledge-catalog/personal_info.md`, `knowledge-catalog/education.md`, and `knowledge-catalog/experience.md`.

2. **Extract Details**: Extract the user's Name, Age, Origin, and Current Location from `personal_info.md`, along with any relevant professional/educational details if asked.

3. **Format the Response Base**: Formulate the response precisely as: "Hello {Name}, {Age}, coming from {Origin}, and currently living in {Location}". Substitute the values you found in the files.

4. **LinkedIn Information**: First, check if a LinkedIn URL is already provided in the OKF files (e.g., in `personal_info.md`). If it is, use that URL. ONLY if it is missing should you use the `search_web` tool to search the web for a LinkedIn profile matching the user's Name and Professional Experience.

5. **Final Output**: Append the LinkedIn URL (either found locally or via web search) to your answer. Ensure the final answer to the user includes both the formatted base string and the LinkedIn link. Do not ask for confirmation before outputting the final result.
