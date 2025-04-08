from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializers(ModelSerializer):
    number_of_lessons = SerializerMethodField()
    lessons = LessonSerializer(many=True)

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ("title", "description", "number_of_lessons")
