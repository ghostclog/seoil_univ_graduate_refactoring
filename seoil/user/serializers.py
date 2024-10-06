from .models import Users,Messages,UserItems
from rest_framework import serializers
from team.models import Teams

class UserRegistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'username',
            'password',
            'nickname'
        )
    def create(self, validated_data):
        user = Users.objects.create(
            username=validated_data['username'],
            nickname=validated_data['nickname'],
        )
        user.set_password(validated_data['password'])  # 비밀번호 암호화
        user.save()
        return user

# 마이페이지용 시리얼라이저.
# 유저 기본 정보 제공
class UserSerializerForMyPage(serializers.ModelSerializer):
    num_of_posts = serializers.SerializerMethodField()
    num_of_comments = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = (
            'nickname',
            'user_comment',
            'user_point',
            'user_profile_photo',
            'num_of_posts',
            'num_of_comments'
        )

    def get_num_of_posts(self, obj):
        return obj.num_of_posts()

    def get_num_of_comments(self, obj):
        return obj.num_of_comments()
    
# 간단 유저 시리얼라이저.
# 마이페이지 내에서 특정 팀에 소속한 팀원 혹은 팀 검색에서 팀에 속한 인원을 보여줄때 사용
class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'nickname',
            'user_profile_photo',
        )

# 이름만 추출하기 용도
class SimpleNicknameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('nickname',)

# 마이페이지에서 팀 선택시 사용되는 시리얼라이저.
# 어쩌면 팀 페이지 내에서도 사용될지도..?
class TeammateSerializerForMyPage(serializers.ModelSerializer):
    team_master = SimpleNicknameSerializer(read_only=True)
    members = SimpleUserSerializer(
        many=True,
        read_only =True,
    )
    class Meta:
        model = Teams
        fields = (
            'team_name',
            'team_master',
            'members',
        )

# 마이페이지의 팀 리스트에 사용
# 팀명과 팀원수를 표시
class UsingTeamList(serializers.ModelSerializer):
    num_of_teamate = serializers.SerializerMethodField()
    class Meta:
        model = Teams
        fields = (
            'team_name',
            'num_of_teamate'
        )
    def get_num_of_teamate(self, obj):
        return obj.num_of_teamate()
# 역참조를 사용
class TeamListSerializerForMypage(serializers.ModelSerializer):
    teams = UsingTeamList(many=True, read_only=True)
    class Meta:
        model = Users
        fields = (
            'teams'
        )

