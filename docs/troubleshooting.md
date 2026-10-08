# Troubleshooting

## Connecting and signing in

**The sign-in page does not open, or sign-in loops.**
Remove the NyayAssist connector from your app, add it again and reconnect.
Allow pop-ups for your AI app, and finish sign-in in the same browser profile.

**"Unauthorized" or `401` when I open the server URL in a browser.**
That is expected. The URL is for MCP clients, which use it to start sign-in.

**Signed in, but my matters and documents are missing.**
Check that you signed in with the same account you use on nyayassist.ai and
that the server URL is `https://mcp.nyayassist.ai/mcp`.

**The connector worked before and now asks me to sign in again.**
Your session expired or was revoked. Reconnect from your app's connector
settings.

**My app supports only local servers.**
See [setup/other-clients.md](setup/other-clients.md#clients-without-remote-oauth-support).

## Tool calls

**"Not found" for a matter, document, draft or job.**
Handles come only from earlier results, belong to the account that received
them and can go stale. Ask the assistant to list the item again.

**"Limit reached" or "not available on your plan".**
Ask the assistant to run `get_my_plan_and_usage`. Allowances and plans are the
same as in the web app; see https://nyayassist.ai/pricing.

**A matter is locked.**
Locked matters cannot be read on the current plan. Review your plan in the
NyayAssist web app.

**Too many requests.**
Calls are rate-limited per user. Wait a minute and try again.

**The result says a job is running.**
Long work runs as a job. The assistant should call `get_job_status`, wait for
the suggested interval, then call `get_job_result`. Use `list_my_jobs` if a job
ID was lost. Do not start the same work again while a job is running; it would
use your allowance twice.

**A document link could not be accessed.**
`file_url` must be a direct, public https download link. Sharing or preview
pages (for example, a Google Drive or Dropbox page) do not work. Use a direct
download link, an upload from your computer, or the web app.

**I cannot read the full judgment, Act, transcript or due-diligence report.**
The connector returns details and summaries for judgments and Acts, metadata
for meetings and report metadata for due diligence. Read the full text in the
NyayAssist web app.

**Workflow approval is refused.**
Through the connector, a workflow review step can only be rejected or
cancelled. Approve or continue it in the web app.

**The notetaker did not join, or Zoom fails.**
`start_meeting` supports Google Meet and Microsoft Teams links only. The host
may need to admit the notetaker from the waiting room.

## Still stuck?

Email support@nyayassist.ai with your app's name, the time of the problem and
the message you saw. Do not send passwords or tokens.
