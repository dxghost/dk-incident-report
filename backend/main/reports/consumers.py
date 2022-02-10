from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ReportConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("reports", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("reports", self.channel_name)
    async def publish_report(self, event):
        await self.send_json(event)