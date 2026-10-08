# Frequently asked questions

**What is the NyayAssist MCP connector?**
A hosted server that lets AI apps such as Claude, ChatGPT, Gemini CLI, Cursor
and VS Code use your NyayAssist account through the Model Context Protocol.

**Do I need a NyayAssist account?**
Yes. You sign in with your NyayAssist account. You can create one at
https://nyayassist.ai.

**Does it cost extra?**
No separate fee. The connector is available on every NyayAssist plan and uses
the same allowances as the web app. Your AI app may have its own plan
requirements for custom connectors.

**Is there anything to install or host?**
No. The server is run by NyayAssist. Some apps install a small package from
this repository (an extension or plugin) that only points at the server and
adds skills.

**Is the server open source?**
No. This repository contains the public packaging and documentation only.

**Can the assistant delete or share my work?**
No. No tool can delete, overwrite, share or send anything. The only tool that
acts outside NyayAssist is `start_meeting`, which sends a notetaker into the
call you name.

**Will it use my plan allowance without asking?**
Tools that create work use your allowance. Most AI apps ask for confirmation
before such a call, and the server tells the assistant to create work only
when you ask for it. Check `get_my_plan_and_usage` before a long task.

**Is the output legal advice?**
No. NyayAssist output is research and drafting support for a qualified
advocate to verify. Check every citation, section and date against the source.

**Can it read full judgments and Acts?**
It returns details and the Legal Library summary or abstract. The full text is
read in the NyayAssist web app.

**Which languages can it translate into?**
Bengali, English, Gujarati, Hindi, Kannada, Malayalam, Marathi, Tamil, Telugu
and Urdu.

**I use NyayAssist Enterprise. How do I connect?**
NyayAssist Enterprise customers: your organisation receives its own setup
instructions from your NyayAssist account team.

**Where is my data stored?**
In your NyayAssist account, under the NyayAssist
[Privacy Policy](https://nyayassist.ai/privacy). Your AI app also processes the
conversation under its own terms.

**How do I disconnect?**
Remove or disconnect NyayAssist in your AI app's connector settings.

**Who do I contact?**
support@nyayassist.ai.
