# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Frames(Model):
    """The response for a Get Frames request.

    :param review_id: Id of the review.
    :type review_id: str
    :param video_frames:
    :type video_frames:
     list[~azure.cognitiveservices.vision.contentmoderator.models.Frame]
    """

    _attribute_map = {
        'review_id': {'key': 'ReviewId', 'type': 'str'},
        'video_frames': {'key': 'VideoFrames', 'type': '[Frame]'},
    }

    def __init__(self, review_id=None, video_frames=None):
        super(Frames, self).__init__()
        self.review_id = review_id
        self.video_frames = video_frames
