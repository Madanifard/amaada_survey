from celery import shared_task
from survey.models.responses import Responses


@shared_task
def save_response_task(user_id: int, question_id: int, option_id: int, answer_text: str):
    try:
        response = Responses(user_id=user_id,
                             question_id=question_id,
                             option_id=option_id,
                             answer_text=answer_text)
        response.save()
        return {'status': 'success', 'response_id': response.id}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
