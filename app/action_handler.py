from video_actions import VideoActions
from video_action_validations import VideoActionValidations

def action_handler(method_name, form, **kw):

    """ Handle an action against the api, from start to end """
    validation_method = getattr(VideoActionValidations, method_name)
    if not validation_method(method_name, form, **kw): return

    action_method = getattr(VideoActions, method_name)
    return action_method(form = form, **kw)




