import video_actions
import video_action_validations

def action_handler(method_name, **kw):

    """ Handle an action against the api, from start to end """
    validation_method = getattr(video_action_validations.VideoActionValidations, method_name)
    if not validation_method(method_name, **kw): return

    action_method = getattr(video_actions.VideoActions, method_name)
    return action_method(**kw)




