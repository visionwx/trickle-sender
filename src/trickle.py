import requests
from unitls import generateUUID
import json

class TrickleClient:
    DOMAIN = "https://api.trickle.so"

    def __init__(self, token):
        self.token = token

    ###
    # Create Trickle API
    def createTrickle(self, workspaceId, memberId, 
        channelId, blocks):
        resp = requests.post(
            url=self.DOMAIN + "/f2b/v1/workspaces/" + workspaceId + "/groups/" + channelId + "/trickles", 
            json={
                "blocks": blocks,
                "authorMemberId": memberId,
                "mentionedMemberIds": [],
                "referTrickleIds": [],
                "tagIds": []
            }, 
            headers={"Authorization": "Bearer " + self.token}
        )
        print(resp.status_code)
        print(resp)
        print(resp.text)

        if not (resp.status_code != 201 or resp.status_code != 200):
            raise Exception("createTrickleFailed")
    
    def deleteTrickle(self, workspaceId, memberId, trickleId):
        # https://api.trickle.so/f2b/v1/workspaces/364397913113100291/trickles/472094857876209672

        resp = requests.delete(
            url=self.DOMAIN + "/f2b/v1/workspaces/" + workspaceId + "/trickles/" + trickleId, 
            json={
                "memberId": memberId
            }, 
            headers={"Authorization": "Bearer " + self.token}
        )
        print(resp.status_code)
        print(resp.text)

        if not (resp.status_code != 201 or resp.status_code != 200):
            raise Exception("createTrickleFailed")

    ###
    # Create Trickle Comment API
    def createTrickleComment(self, workspaceId, memberId, 
        trickleId, blocks):
        resp = requests.post(
            url=self.DOMAIN + "/f2b/v1/workspaces/" + workspaceId + "/trickles/" + trickleId + "/comments", 
            json={
                "blocks": blocks,
                "authorMemberId": memberId,
                "mentionedMemberIds": []
            }, 
            headers={"Authorization": "Bearer " + self.token}
        )
        print(resp.status_code)
        print(resp)
        print(resp.text)

        if not (resp.status_code != 201 or resp.status_code != 200):
            raise Exception("createTrickleCommentFailed")
    pass

if __name__ == "__main__":
    # blocks = [
    #     {
    #     "id": generateUUID(),
    #     "type": "rich_texts",
    #     "isFirst": False,
    #     "indent": 0,
    #     "blocks": [],
    #     "display": "block",
    #     "elements": [
    #         {
    #         "id": generateUUID(),
    #         "type": "text",
    #         "text": "Hello World Test 2",
    #         "elements": [],
    #         "isCurrent": True
    #         }
    #     ],
    #     "isCurrent": True,
    #     "constraint": "free"
    #     }
    # ]
    # print(blocks)
    tc = TrickleClient(token="xxxx")
    # tc.createTrickle(
    #     workspaceId="364397913113100291",
    #     memberId="364404407103651845",
    #     channelId="364397913113165830",
    #     blocks=blocks
    # )
    # tc.createTrickleComment(
    #     workspaceId="364397913113100291",
    #     memberId="364404407103651845",
    #     trickleId="578759146069819400",
    #     blocks=blocks
    # )