import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_box_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.group_name = "chat_%s" % self.chat_box_name
        # print(self.group_name)
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        print("connect",self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        print("disconnect")
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json,"from react")
        message = text_data_json["message"]
        username = text_data_json["username"]
        # await self.save_message(username, room, message)


        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chatbox_message",
                "message": message,
                "username": username,
                "receiver":text_data_json["receiver"],
                "user_channel":text_data_json["user_channel"]
            },
        )
  
    async def chatbox_message(self, event):
        message = event["message"]
        username = event["username"]

        #send message and username of sender to websocket
        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "username": username,
                    "receiver":event["receiver"],
                    "user_channel":event["user_channel"]
                }
            )
        )

    
    # @sync_to_async
    # def save_message(self, username, room, message):
    #     user = User.objects.get(username=username)
    #     room = Room.objects.get(slug=room)

    #     Message.objects.create(user=user, room=room, content=message)
