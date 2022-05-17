#!/usr/bin/env python

import requests
from ansible.module_utils.basic import AnsibleModule


def main() -> None:
    module_args = dict(
        url=dict(type="str", required=True),
        role_name=dict(type="str", required=True),
        token=dict(type="str", required=True),
        common_name=dict(type="str", required=True),
        alt_names=dict(type="list", elements="str", required=False, default=[]),
    )

    module = AnsibleModule(argument_spec=module_args)

    try:
        data = requests.post(
            url=f"{module.params['url']}/v1/pki_int/issue/{module.params['role_name']}",
            headers={
                "X-Vault-Token": module.params["token"],
            },
            json=dict(
                common_name=module.params["common_name"],
                alt_names=",".join(module.params["alt_names"]),
                format="pem",
            ),
            verify=False,
        )

        if not data.ok:
            module.fail_json(
                msg="Error happened when issuing certificate",
                response=data.json(),
                changed=False,
            )

        module.exit_json(data=data.json(), changed=True)

    except requests.exceptions.RequestException as err:
        module.fail_json(
            msg="Error happened when issuing certificate",
            err=err.strerror,
            changed=False,
        )


if __name__ == "__main__":
    main()
