from materials.models import Course, Lesson, Subscription
from materials.validators import LinkValidator
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LinkValidator(field="link")]


class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializers(ModelSerializer):
    number_of_lessons = SerializerMethodField()
    lessons = LessonSerializer(many=True)

    subscription = SerializerMethodField()

    def get_subscription(self, course):
        user = self.context["request"].user
        return (
            Subscription.objects.all().filter(user=user).filter(course=course).exists()
        )

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ("title", "description", "number_of_lessons", "subscription")


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = ("sign_of_subscription",)
