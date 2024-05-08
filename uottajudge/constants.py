ANNOTATOR_ID = 'annotator_id'
TELEMETRY_URL = 'https://telemetry.anish.io/api/v1/submit'
TELEMETRY_DELTA = 20 * 60 # seconds
SENDGRID_URL = "https://api.sendgrid.com/v3/mail/send"

# Setting
# keys
SETTING_CLOSED = 'closed' # boolean
SETTING_TELEMETRY_LAST_SENT = 'telemetry_sent_time' # integer
# values
SETTING_TRUE = 'true'
SETTING_FALSE = 'false'

# Defaults
# these can be overridden via the config file
DEFAULT_WELCOME_MESSAGE = '''
Welcome to **uOttaJudge**. 🎉

**Before proceeding, kindly review this important message.** 📝

uOttaJudge is an automated expo judging system designed to guide you through the judging process while collecting your votes seamlessly. 🤖

The system operates on a pairwise comparison model. You'll begin by reviewing a single submission. Subsequently, for each new submission, you'll determine whether it surpasses or falls short of the previous one **without delay**. 🔄

Should you encounter difficulty locating a specific submission, utilize the 'Skip' button for reassignment. **Avoid skipping unless absolutely necessary**. ⚠️

Submitting votes via uOttaJudge is straightforward, yet it's crucial to deliberate before casting your vote. **Once a decision is made, it cannot be reversed**. ⏳
'''.strip()

DEFAULT_EMAIL_SUBJECT = 'Welcome to uOttaJudge!'

DEFAULT_EMAIL_BODY = '''
Hi {name},

Welcome to uOttaJudge, the online expo judging system. This email contains your
magic link to the judging system.

DO NOT SHARE this email with others, as it contains your personal magic link.

To access the system, visit {link}.

Once you're in, please take the time to read the welcome message and
instructions before continuing.
'''.strip()

DEFAULT_CLOSED_MESSAGE = '''
The judging system is currently closed. Reload the page to try again.
'''.strip()

DEFAULT_DISABLED_MESSAGE = '''
Your account is currently disabled. Reload the page to try again.
'''.strip()

DEFAULT_LOGGED_OUT_MESSAGE = '''
You are currently logged out. Open your magic link to get started.
'''.strip()

DEFAULT_WAIT_MESSAGE = '''
Wait for a little bit and reload the page to try again.

If you've looked at all the projects already, then you're done.
'''.strip()
