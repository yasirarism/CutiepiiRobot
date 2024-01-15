import json

import requests
from telegram.ext import CommandHandler, run_async

from Cutiepii_Robot import dispatcher
from Cutiepii_Robot.modules.helper_funcs.alternate import send_message
from Cutiepii_Robot.modules.helper_funcs.chat_status import user_admin


@run_async
@user_admin
def phone(update, context):

    args = update.effective_message.text.split(None, 1)
    information = args[1]
    key = "fe65b94e78fc2e3234c1c6ed1b771abd"
    number = information
    api = f"http://apilayer.net/api/validate?access_key={key}&number={number}&country_code=&format=1"
    output = requests.get(api)
    content = output.text
    obj = json.loads(content)
    country_code = obj["country_code"]
    country_name = obj["country_name"]
    location = obj["location"]
    carrier = obj["carrier"]
    line_type = obj["line_type"]
    validornot = obj["valid"]
    aa = f"Valid: {str(validornot)}"
    a = f"Phone number: {str(number)}"
    b = f"Country: {str(country_code)}"
    c = f"Country Name: {str(country_name)}"
    d = f"Location: {str(location)}"
    e = f"Carrier: {str(carrier)}"
    f = f"Device: {str(line_type)}"
    g = f"{aa}\n{a}\n{b}\n{c}\n{d}\n{e}\n{f}"
    send_message(update.effective_message, g)


PHONE_HANDLER = CommandHandler("phone", phone)

dispatcher.add_handler(PHONE_HANDLER)


__command_list__ = ["phone"]
__handlers__ = [PHONE_HANDLER]
