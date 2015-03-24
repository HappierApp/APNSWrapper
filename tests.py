#!/usr/bin/env python
"""
 tests.py
 wrapper

 Created by max klymyshyn on 11/15/09.
 Copyright (c) 2009 Sonettic. All rights reserved.
"""

from APNSWrapper import (APNSNotification, APNSAlert, APNSNotificationWrapper,
                         APNSFeedbackWrapper)
import base64
import argparse


def badge(wrapper, token):
    message = APNSNotification()
    message.tokenBase64(token)

    message.badge(3)
    print message
    wrapper.append(message)


def sound(wrapper, token):
    message = APNSNotification()
    message.tokenBase64(token)

    message.sound("default")
    print message
    wrapper.append(message)


def alert(wrapper, token):
    message = APNSNotification()
    message.tokenBase64(token)

    apns_alert = APNSAlert()
    apns_alert.body("Very important alert message")

    apns_alert.loc_key("ALERTMSG")

    apns_alert.loc_args(["arg1", "arg2"])
    apns_alert.action_loc_key("OPEN")

    message.alert(apns_alert)

    # properties wrapper
    message.setProperty("acme", (1, "custom string argument"))

    print message
    wrapper.append(message)


def testAPNSWrapper(encoded_token, cert_path, sandbox=True):
    """
    Method to testing apns-wrapper module.
    """

    wrapper = APNSNotificationWrapper(cert_path,
                                      sandbox=sandbox,
                                      debug_ssl=True,
                                      force_ssl_command=False)
    badge(wrapper, encoded_token)
    sound(wrapper, encoded_token)
    alert(wrapper, encoded_token)
    wrapper.connect()
    wrapper.notify()
    wrapper.disconnect()

    feedback = APNSFeedbackWrapper(cert_path,
                                   sandbox=sandbox,
                                   debug_ssl=True,
                                   force_ssl_command=False)
    feedback.receive()

    print "\n".join(["> " + base64.standard_b64encode(y) for x, y in feedback])


def main():
    parser = argparse.ArgumentParser(description="Run the APNSWrapper Tests.")
    parser.add_argument("apns_token", help="APNS Token to send to.")
    parser.add_argument("-c", "--cert", default='iphone_cert.pem',
                        help="APNS Certificate to use.")

    arguments = parser.parse_args()
    testAPNSWrapper(arguments.apns_token, arguments.cert, False)

if __name__ == "__main__":
    main()
