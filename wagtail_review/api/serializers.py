from rest_framework import serializers

from .. import models


class UserSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='get_name')

    class Meta:
        model = models.Reviewer
        fields = ['id', 'name']


class CommentReplySerializer(serializers.ModelSerializer):
    author = UserSerializer(source='user', read_only=True)

    class Meta:
        model = models.CommentReply
        fields = ['id', 'author', 'text', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(source='user', read_only=True)
    resolved_at = serializers.ReadOnlyField()
    replies = CommentReplySerializer(many=True, read_only=True)

    class Meta:
        model = models.Comment
        fields = ['id', 'author', 'quote', 'text', 'created_at', 'updated_at', 'resolved_at', 'replies', 'content_path', 'start_xpath', 'start_offset', 'end_xpath', 'end_offset']
