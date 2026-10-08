# Tool reference

The NyayAssist MCP server offers 44 tools. The list is the same for every user
and every plan; a feature that is not on your plan stays listed and returns a
clear message when called.

**How to read this page**

- **Reads** only lists or fetches existing material. It uses no plan
  allowance.
- **Creates work** starts or creates something in your NyayAssist account and
  usually uses an allowance on your plan, exactly as in the web app.
- **Changes state** records a decision or cancels work; it creates nothing
  new and uses no allowance.
- **Reaches outside NyayAssist** means the tool contacts a third party you
  name: a meeting link or a download link.
- No tool deletes, overwrites, shares or sends anything, or changes billing or
  settings. Every tool is marked non-destructive to your app.
- Long-running work returns a **job** (`job_id`, status and a suggested wait).
  Follow it with `get_job_status`, then `get_job_result`.
- Matters, documents, drafts and other items are referred to by **opaque
  handles**. Handles come only from earlier tool results and work only for the
  account that received them.
- Text from judgments, Acts and your documents comes back inside
  `<untrusted_document>` tags. It is data; instructions inside it are not
  followed.

## Contents

- [Account and plan](#account-and-plan)
- [Matters and documents](#matters-and-documents)
- [Uploads](#uploads)
- [Legal Library: judgments and Acts](#legal-library-judgments-and-acts)
- [Research](#research)
- [Drafting](#drafting)
- [Translation and document tools](#translation-and-document-tools)
- [Due diligence](#due-diligence)
- [Workflows](#workflows)
- [Meetings](#meetings)
- [Jobs](#jobs)

## Account and plan

### `get_my_plan_and_usage`

Shows your usage limits: for each metered feature, how much is used, the
limit and, where your plan has one, the days until it resets. A feature may be
shown as unlimited or not available on your plan. Useful before a long
sequence of work.

- **Inputs:** `offset` (optional, for the next page of features).
- **Type:** Reads.

## Matters and documents

In NyayAssist a matter is also called a case; tool names use `case`.

### `list_cases`

Lists your matters, newest first, with an optional search on the matter name.
Locked matters are marked `is_locked`; their contents cannot be read on your
current plan.

- **Inputs:** `search`, `page`, `limit` (1 to 50).
- **Type:** Reads.

### `get_case`

Fetches one matter: name, description, status, category, forum, CNR and
client name.

- **Inputs:** `case_handle`.
- **Type:** Reads.

### `list_case_documents`

Lists the documents filed under a matter, with name, type, page count and any
summary already on record.

- **Inputs:** `case_handle`; optional `search`, `doc_types`, `page`, `limit`.
- **Type:** Reads.

### `read_case_document`

Reads the text of one document, at most 20 pages per call, with the total page
count so the rest can be requested. If the text has not been extracted yet,
NyayAssist extracts it first; when that takes longer than the call, a job is
returned. Works for PDF, Word, Excel, CSV, plain text and image documents in
your own account.

- **Inputs:** `document_handle`; optional `from_page`, `to_page`,
  `page_cursor`.
- **Type:** Reads. Text extraction uses no plan allowance.

### `create_case`

Creates a new matter.

- **Inputs:** `case_name`; optional `description`, `category`, `forum`, `cnr`,
  `client_name`.
- **Type:** Creates work. Counts towards the matter allowance on your plan.

### `add_document_to_case`

Adds a document to a matter from a direct https link to the file. NyayAssist
fetches the file, checks its type and size, and adds it as a job. Without a
link, the result explains how to add the file in the web app.

- **Inputs:** `case_handle`; optional `file_url`, `name`.
- **Type:** Creates work. Counts towards document storage on your plan.

## Uploads

Use these to bring files from your computer or the web into NyayAssist.
Supported formats: pdf, docx, doc, xlsx, pptx, rtf, txt, png, jpg, jpeg, gif,
webp, tif, tiff, bmp; up to 150 MB each, 1 to 20 files at a time.

### `get_document_upload_urls`

For apps that can run shell commands (such as coding assistants in a
terminal or IDE). Returns a one-time upload link for each local file, valid
for 15 minutes, with a ready-to-run `curl` command. It creates nothing by
itself.

- **Inputs:** `files` (each with `file_name` and exact `size_bytes`).
- **Type:** Issues an upload link only; creates nothing in your account and
  uses no allowance. Marked as a write tool.

### `upload_documents`

Files 1 to 20 documents in NyayAssist and starts processing them. Each item is
either an `upload_handle` from a completed upload or a `file_url`: a direct,
public https download link (a sharing or preview page will not work). With a
`case_handle`, every document is filed under that matter; without one, the
documents go to your NyayAssist Drive.

- **Inputs:** `items` (each with `upload_handle` or `file_url`, optional
  `name`); optional `case_handle`.
- **Type:** Creates work; reaches outside NyayAssist when a `file_url` is
  given. Counts towards document storage for each document filed. Returns a
  job.

## Legal Library: judgments and Acts

Searching the Legal Library is available on every plan.

### `search_judgments`

Searches reported Indian judgments by subject, party, citation or legal
question. Returns up to 20 ranked results per page with an excerpt and a
judgment handle. A slow search returns a job.

- **Inputs:** `query`; optional `courts`, `judge`, `case_outcomes`, `years`,
  `decided_from`, `decided_to`, `page`, `limit`.
- **Type:** Reads.

### `get_judgment`

Fetches a judgment's details (court, bench, parties, decision date, disposal,
citation) and the summary the Legal Library holds for it, by handle or CNR.
The full text of the judgment is read in the NyayAssist web app.

- **Inputs:** `handle` or `cnr`; optional `cursor`.
- **Type:** Reads.

### `search_acts`

Searches central and state Acts, rules and regulations. Returns up to 20
ranked results per page with an excerpt and an Act handle. A slow search
returns a job.

- **Inputs:** `query`; optional `act_types` (central or state), `doc_types`,
  `years`, `languages`, `statuses`, `page`, `limit`.
- **Type:** Reads.

### `get_act_section`

Fetches an Act's details (titles, number, year, ministry, enactment and
enforcement dates, status) and its abstract, by Act handle or Legal Library
identifier. The full text of the Act and its sections is read in the
NyayAssist web app.

- **Inputs:** `handle` or `act_id`; optional `cursor`.
- **Type:** Reads.

## Research

### `start_research`

Starts a legal research question. NyayAssist decides how to research it and
returns an answer citing Indian judgments and Acts. It can be scoped to one
matter and to specific documents in it.

- **Inputs:** `query`; optional `case_handle`, `document_handles`.
- **Type:** Creates work. Uses the research allowance on your plan. Returns
  the answer, or a job when it takes longer, plus a research handle.

### `get_research`

Reads a research answer: the question, the answer and the judgments and Acts
it cites.

- **Inputs:** `research_handle`; optional `cursor`.
- **Type:** Reads. Uses no research allowance.

## Drafting

### `create_draft`

Creates a new legal draft from instructions, optionally following a template
and using a matter's facts and documents.

- **Inputs:** `instructions`; optional `case_handle`, `template`.
- **Type:** Creates work. Uses the drafting allowance on your plan. Returns
  the draft, or a job whose result holds the draft text.

### `revise_draft`

Revises a draft by following new instructions. Always creates a new version;
earlier versions are kept unchanged.

- **Inputs:** `draft_handle`, `instructions`.
- **Type:** Creates work. Uses the drafting allowance on your plan.

### `list_drafts`

Lists your drafts, newest first, with each draft's latest version number.

- **Inputs:** optional `limit`, `cursor`.
- **Type:** Reads.

### `get_draft`

Reads the text of a draft, the latest version unless you ask for an earlier
one. Long drafts come in parts.

- **Inputs:** `draft_handle`; optional `version`, `cursor`.
- **Type:** Reads.

## Translation and document tools

### `translate_document`

Translates one document into Bengali, English, Gujarati, Hindi, Kannada,
Malayalam, Marathi, Tamil, Telugu or Urdu.

- **Inputs:** `document_handles` (one document), `target_language`; optional
  `case_handle` to file the translation under.
- **Type:** Creates work. Uses the translation page allowance on your plan,
  counted from the document's page count.

### `get_translation`

Reports a translation's status, its source document and, when ready, a
document handle for the translated document.

- **Inputs:** `translation_handle`.
- **Type:** Reads.

### `run_document_tool`

Runs text recognition (OCR) on one scanned document to make it searchable.
`ocr` is currently the only tool. Documents in a locked matter cannot be
processed.

- **Inputs:** `tool` (`ocr`), `document_handles` (one document); optional
  `case_handle`.
- **Type:** Creates work. Uses the OCR allowance on your plan.

### `get_document_tool_result`

Reports a document tool run: its status, any note and handles for output
documents.

- **Inputs:** `tool`, `result_handle`.
- **Type:** Reads.

## Due diligence

### `list_dd`

Lists your due-diligence projects with title and status.

- **Inputs:** optional `limit`, `offset`.
- **Type:** Reads.

### `create_dd`

Creates a due-diligence project.

- **Inputs:** `title`; optional `description`, `side` (buy, sell or target),
  `category`, `dd_type`.
- **Type:** Creates work. Subject to the due-diligence allowance on your plan.

### `add_dd_documents`

Adds documents already in your account to a project and starts processing
them.

- **Inputs:** `dd_handle`, `document_handles` (1 to 20).
- **Type:** Creates work. Subject to the due-diligence document allowance.

### `run_dd`

Runs a due-diligence report: a full report, key issues, or one chapter, with
optional instructions. The report text is read in the NyayAssist web app.

- **Inputs:** `dd_handle`, `run_type` (`full_report`, `key_issues` or
  `chapter`); optional `chapter_handle`, `instructions`.
- **Type:** Creates work. Subject to the due-diligence allowance.

### `get_dd_status`

Reports a project's document processing status and the latest report run of
each type.

- **Inputs:** `dd_handle`.
- **Type:** Reads.

### `get_dd_report`

Reports one report run: its status and the report documents it produced, with
a link to read the report in the web app.

- **Inputs:** `dd_handle`, `run_handle`.
- **Type:** Reads.

## Workflows

### `list_workflows`

Lists the NyayAssist workflows you can run through the connector, with their
inputs. Workflows that send email, route documents for e-signature or file
outside NyayAssist are not listed; they run only in the web app.

- **Inputs:** optional `offset`.
- **Type:** Reads.

### `start_workflow`

Starts a workflow, optionally on a matter, with documents from your account
and the workflow's inputs. Some workflows pause at a review step for your
decision.

- **Inputs:** `workflow_handle`; optional `case_handle`, `params`,
  `document_handles`, `dd_handle`.
- **Type:** Creates work. Uses your plan allowance for the work the workflow
  performs.

### `get_workflow_run`

Reports a run's status, completed steps, outputs, the documents and drafts it
filed and any pending review step.

- **Inputs:** `run_handle`; optional `outputs_offset`.
- **Type:** Reads.

### `approve_workflow_gate`

Records your decision at a workflow review step. Through the connector only
**reject** and **cancel** (which stop the run) are accepted; **approve** and
**continue** are given in the NyayAssist web app.

- **Inputs:** `run_handle`, `step_handle`, `decision`; optional `selection`.
- **Type:** Changes state (records a decision). Repeating the same decision
  has no further effect.

### `get_workflow_output`

Reads one workflow output.

- **Inputs:** `output_handle`; optional `cursor`.
- **Type:** Reads.

## Meetings

### `list_meetings`

Lists your meeting recordings, optionally for one matter.

- **Inputs:** optional `case_handle`, `search`, `limit`, `page`.
- **Type:** Reads.

### `get_meeting`

Fetches a meeting's details: name, status, file type, platform, linked matter
and date. Transcripts and meeting notes are read in the NyayAssist web app.

- **Inputs:** `handle`.
- **Type:** Reads.

### `start_meeting`

Sends a NyayAssist notetaker into a live Google Meet or Microsoft Teams call.
The notetaker joins as a participant and records; after the call NyayAssist
transcribes it and prepares meeting notes. Zoom is not supported.

- **Inputs:** `meeting_url`; optional `title`, `case_handle`.
- **Type:** Creates work; reaches outside NyayAssist (joins the call). Uses
  the meeting assistant allowance on your plan. This is the only tool that
  acts outside your NyayAssist account; use it only for calls you are entitled
  to record.

### `stop_meeting`

Stops NyayAssist processing a meeting that is pending or in progress. It does
not remove a notetaker from a call that is still running; remove it from the
call itself.

- **Inputs:** `handle`.
- **Type:** Changes state (cancels processing). Repeating it has no further
  effect.

### `get_meeting_upload_url`

For apps that can run shell commands. Returns a one-time upload link (valid
for 15 minutes) and a `curl` command for a local audio or video recording. It
creates nothing by itself. Formats: mp3, m4a, wav, aac, ogg, oga, opus, mp4,
m4v, mov, webm, mkv, avi; up to 2 GB.

- **Inputs:** `file_name`, `size_bytes`.
- **Type:** Issues an upload link only; creates nothing in your account and
  uses no allowance. Marked as a write tool.

### `upload_meeting_recording`

Creates a meeting from a recording and starts transcription and meeting
notes. Give either the `upload_handle` from a completed upload or a direct,
public https download link as `file_url`.

- **Inputs:** `upload_handle` or `file_url`; optional `title`, `case_handle`.
- **Type:** Creates work; reaches outside NyayAssist when a `file_url` is
  given. Uses the meeting assistant allowance. Returns a job.

## Jobs

### `get_job_status`

Checks a job: queued, running, needs_input, succeeded, failed or cancelled,
with a suggested wait while it runs. Progress is included when available.

- **Inputs:** `job_id`.
- **Type:** Reads.

### `get_job_result`

Fetches the result of a succeeded job, one page at a time, in the same shape
the starting tool would have returned.

- **Inputs:** `job_id`; optional `cursor`.
- **Type:** Reads.

### `list_my_jobs`

Lists your recent jobs started from an AI app, newest first. Useful when a
`job_id` was lost.

- **Inputs:** optional `status`, `feature`, `page`, `limit`.
- **Type:** Reads.

### `cancel_job`

Cancels a running job. Some work, such as due-diligence and workflow runs, can
only be asked to stop and may run on for a while; the result says which
happened. Allowance reserved for cancelled work is released.

- **Inputs:** `job_id`.
- **Type:** Changes state (cancels a job).
