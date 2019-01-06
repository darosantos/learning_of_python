def show_confirm_dialog(msg, msg_button=''):
    confirm = input(msg + ' ' + msg_button)
    if confirm.lower() == 's':
        return True
    else:
        return False