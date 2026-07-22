---
name: job-tailoring
description: Help tailor a resume and application assets for a specific job posting or description.
---

# /job-tailoring Agent Skill

**Trigger**: `/job-tailoring` or requests like "I have this Job posting with the following job description or job posting link, I want you to help me to tailor my resume for this offer"

## Overview
This skill assists the user in tailoring their resume and application for a specific job offer. It requires the user's current information (from context, OKF markdown files, or an attached resume) and the job description.

## Steps

Follow these steps strictly. This skill uses a **Human-in-the-Loop** approach. At specific steps, you MUST stop and ask the user for input or approval, waiting for their response before proceeding.

### Step 1: Extract and Analyze Job Description
- Extract, analyze, and read the JOB description from all the listed sources provided by the user (links or text).

### Step 2: Initialize Workspace
- Extract the `[Company]` and `[Role]` from the job description.
- Create a new directory at the active workspace root: `./JOB Applications/[Company] - [Role]/`.
- Create a file inside this folder named `1 - Job Description Details.md`.
- Save the complete, unedited raw job description along with the URL (if it exists) into this file.

### Step 3: Grouping Method Breakdown
- Analyze the job description and use the "Grouping Method Overview" to break down the job requirements and suitability.
- **Grouping Method Overview**: Group related job requirements and objectives together into categories. This provides a better understanding of the position. Examples:
  - *Financial Skills*: [List of financial skills listed in the JD]
  - *General Office/Management*: [List of General Office or Management Skills listed in the JD]
  - *Technical*: [List of Technical Skills required and listed in the JD]
- Save these results in a file named `2 - Job description breakdown.md` using standard Markdown frontmatter and place it in the folder created for this job application (`./JOB Applications/[Company] - [Role]/`).

### Step 4: Job Matching Summary
- Analyze the results from the Grouping Method and match them with the user's personal profile.
- Score the match on a scale of 1 to 100.
- Create a summary of the skills, responsibilities, duties, and achievements from the profile that highlight and cover the requirements in the JD.
- **CRITICAL**: When listing matching statements, achievements, and responsibilities for each job in the Professional Experience section, you **MUST** use the exact same text/wording as it is written in the source profile. Do NOT rephrase, edit, or summarize the text.
- Save this analysis in a file named `3 - Job Matching Summary.md` using standard Markdown frontmatter and place it in the folder created for this job application.
- **Example Summary Format**:
  - **Skills**: [bullet list of current skills in the profile that match the JD]
  - **Professional Experience**:
    ### [Company] - [Role]
    - [Exact matching statement from source profile 1]
    - [Exact matching statement from source profile 2]

    ### [Company 2] - [Role]
    - [Exact matching statement from source profile 1]


### Step 5: Tailoring Experience (Human-in-the-Loop)
- Take the exact matching statements from Step 4 (grouped by company) and use the P-A-R statement method to rephrase/tailor them according to the job description **no more than 220 characters** (in case they are already tailored).
- **HUMAN-IN-THE-LOOP**: If the profile's experience lacks a specific and important skill or statement, pause and ask the user open questions to identify the achievement and statement. **Wait for the user's response.** Once the user responds, incorporate the feedback.
- To address these modifications/rephrasing/additions and recommendations, use the **P-A-R statement method** (described below). Each statement must be **no more than 220 characters**.
- If additional details/statements were added during the Human-in-the-loop iteration, add those statements to the corresponding company and role sections to which they belong.
- **Formatting & Ordering**: Group everything by `### [Company] - [Role]`. Within each section, place the bullets in the order they were collected: first the rephrased statements from Step 4, followed by the new statements from the Step 5 Human-in-the-loop iteration.
- Once the tailoring is completed, the user has answered the questions and the matching level increased to at least **85%**, save the analysis in a file named `4 - Job Matching Tailoring Experience.md` using standard Markdown frontmatter and place it in the folder created for this job application.

#### P-A-R Statement Method
PAR stands for Problem, Action, Result. It demonstrates the ability to showcase professional achievements, demonstrating your ability to identify issues, take initiative, and deliver tangible results.
- **Problem**: Describe the problem concisely (e.g., "Faced declining customer satisfaction scores due to long response times.").
- **Action**: Use strong action verbs and detail the steps taken (e.g., "Implemented a new ticketing system and developed a knowledge base.").
- **Result**: Quantify achievements using numbers, percentages, or time frames (e.g., "Reduced average response time by 40% and improved customer satisfaction scores from 3.2 to 4.7 within three months.").
- Examples of ordering:
  - *[Problem] [Action] [Result]*
  - *[Action] [Result] [Problem]*
  - *[Result] [Action] [Problem]*

### Step 6: Corporate Intelligence Brief & Professional Statement
- Write a Corporate Intelligence Brief: A concise, 300-word summary detailing what the target company does, its core challenges, and how the user's profile naturally solved their problems.
- Craft a Professional Statement: Around 300 characters or less, using the profile experience and keywords from the JD. Create a powerful value proposition that could attract a Recruiter's attention in under 5 seconds of skimming.
- Write "Career Highlights": A summary of the top 3 highlights that resonate with the Job Description and align with the profile's experience. Make sure these highlights are written using the P-A-R method, are drawn from the professional experience as a summary of the best highlights, and do not repeat the professional experience tailoring. Each highlight must be less than 220 characters.
- Save this in a file named `5 - Tailored Professional Statement and Career Highlights.md` using standard Markdown frontmatter and place it in the folder created for this job application.

### Step 7: Tailored Cover Letter (Human-in-the-Loop)
- Craft a Tailored Cover Letter using the breakdown from the job description, profile information, and tailored experience.
- Use the formatting guide below. Assume **Canadian formatting** rules and best practices for dates and addresses by default, unless otherwise specified.
- **HUMAN-IN-THE-LOOP**: If some details are needed to elaborate further, pause and ask the user questions. **Wait for the user's response.**
- Once complete, save it in a file named `6 - Tailored Cover Letter.md` using standard Markdown frontmatter and place it in the folder created for this job application.

#### Cover Letter Format Guide
- Profile's Name
- Profile's Address/Current Location, City, Province, Postal Code
- Profile's Cellphone number
- Profile's E-Mail Address
- Profile's LinkedIn URL AND/OR professional website's portfolio URL if present.

- *Current Date* (Canadian format)
- *Name of the Hiring Manager* (if present, otherwise placeholder "Hiring Committee")
- *Name of Organization/Company*
- *Address of Organization/Company* (Search for it or add a placeholder)
- *City, Province, Postal Code of the Organization/Company*
- Re: Title of Job or Posting (competition/reference number)

- To the Hiring Committee/Name of the HR Recruiter:
- **Introduction Paragraph (Max 300 characters)**:
  - Name of the position applied for.
  - Briefly state what impresses about the organization and the position.
  - Briefly introduce (list) the experience that makes the profile an excellent fit.
- **Main Body (1-4 paragraphs, Max 250 characters each)**:
  - Elaborate on the experiences introduced in the last sentence(s) of the intro.
  - Restrict each paragraph to one or a related set of experiences.
  - State the main point in the first sentence.
  - Elaborate and quantify/qualify in following sentences.
- **Conclusion and Closing Statements (Max 220 characters)**:
  - Summarize how relevant experience/skills match the JD.
  - Demonstrate knowledge about the organization’s best qualities.
  - Request a personal interview to discuss the position and qualifications.
- Sincerely,
- Profile's Name

**Tone**: Should be written in a similar tone to the rest of the resume and ideally longer than 4 paragraphs in total.

### Step 8: Market & Salary Assessment, Networking Targets, & Interview Prep
- **Market & Salary Assessment (Ontario Focus)**: Analyze the target seniority level. Evaluate the salary against current industry averages in Ontario, Canada (specifically Ottawa/Toronto market rates). If the job posting lists compensation, state whether it is Below Market, At Market, or Above Market. If unlisted, provide the expected regional range.
- **LinkedIn Networking Targets**: Identify 2-3 specific peer or leadership roles within the target company (e.g., "Director of Engineering", "Senior Team Lead") that the user should search for to establish connections.
- **Interview Prep**: Brainstorm possible interview questions and how to answer them according to the profile's experience using the STAR method.
- Save this in a file named `7 - Research Brief.md` using standard Markdown frontmatter and place it in the folder created for this job application.

### Step 9: Final Assessment
- Run a final assessment and matching score.
- Provide a summary of the relevant changes from the initial analysis to the tailoring process, and explain how it improves the profile's application for this Job Description.
