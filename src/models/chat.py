from datetime import datetime

# 1. Пользователь отправляет запрос на поиск собеседника (-ов)
# 2. Сервер ищет собеседника
# 3. После того, как сервер нашёл собеседника, он создаёт несколько объектов:
#    - чат
#    - участников чата

type ParticipantId = int
type ChatId = str
type AccessToken = str


class Participant:
    id: ParticipantId
    access_token: AccessToken


class Message:
    content: str
    data: datetime
    sender_id: ParticipantId


class Chat:
    id: ChatId
    participants: list[Participant]
    message_history: list[Message]
