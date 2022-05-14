#!/usr/bin/env python

import getpass
import os
from ansible.module_utils.basic import AnsibleModule

VERIFICATION_FILE_PATH = os.path.expanduser("~/.verification_email_sent")


def main() -> None:
    module_args = dict(
        recipient=dict(type="str", required=True),
    )

    result = dict(changed=False)

    module = AnsibleModule(argument_spec=module_args)

    if not os.path.exists(VERIFICATION_FILE_PATH):
        os.mknod(VERIFICATION_FILE_PATH)

    with open(VERIFICATION_FILE_PATH, mode="r+", encoding="utf-8") as file:
        lines = file.readlines()
        if len(lines) != 1 or lines[0] != module.params["recipient"]:
            # send out the email
            subject = "Testing email"
            body = f"Hello!\nThis email was sent with sendmail from an ansible module.\nby {getpass.getuser()} from {os.uname()[1]}"

            os.system(
                f"echo -e \"Subject: {subject}\n\n{body}\" | sendmail {module.params['recipient']}"
            )

            result["changed"] = True

            file.seek(0)
            file.write(module.params["recipient"])
            file.truncate()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
