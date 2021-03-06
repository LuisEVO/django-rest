from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Workshop
from .serializers import WorkshopModelSerializer, WorkshopCoverPageModelSerializer,\
    WorkshopTemaryModelSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import api_view


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class WorkshopsViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopModelSerializer
    pagination_class = LargeResultsSetPagination
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['start_date']
    search_fields = ['name']
    permission_classes = [IsAuthenticatedOrReadOnly]


class WorkshopsCoverPageViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopCoverPageModelSerializer
    http_method_names = ['put']
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(
        operation_description="Upload cover image",
        tags=['courses files'],
    )
    def update(self, request, *args, **kwargs):
        return super(WorkshopsCoverPageViewSet, self).update(request, *args, **kwargs)


class WorkshopsTemaryViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopTemaryModelSerializer
    http_method_names = ['put']
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(
        operation_description="Upload temary pdf",
        tags=['courses files'],
    )
    def update(self, request, *args, **kwargs):
        return super(WorkshopsTemaryViewSet, self).update(request, *args, **kwargs)


@swagger_auto_schema(
    method='GET',
    operation_description="populate data",
    tags=['courses populate'],
)
@api_view(['GET'])
def populate_workshops(request):
    Workshop.objects.all().delete()

    Workshop.objects.bulk_create([
        Workshop(
            name="SERVICIOS WEB RESTFUL",
            description="Dise??o, implementaci??n y despliegue de servicios web empresariales basados en JAX-RS (Java API for RESTful Web Services), utilizando Spring Boot, Jersey y RESTEasy con Oracle y JPA/Hibernate/Spring Data. Su testeo se realizar?? v??a POSTMAN y JSONLint, su consumo se implementar?? a nivel de Java (incluye servicios externos).",
            price=420,
            level=[3],
            frequency=[7],
            start_date="2021-09-12",
            start_time="09:30",
            end_time="14:30",
            hours=30,
            sessions=4,
            cover="poster/servicios-web-restful.jpg",
            temary="temary/servicios-web-restful.pdf"
        ),
        Workshop(
            name="DEVOPS FOR JAVA DEVELOPERS",
            description="El profesional al finalizar el curso adquirir?? las siguientes competencias: Interiorizar la cultura DevOps y aplicar los conceptos y tecnolog??as relacionadas. Usar DevOps para entregar soluciones de calidad y de manera continua. Uso de framework, herramientas y tecnolog??as relacionadas con DevOps",
            price=699,
            level=[2],
            frequency=[3, 5],
            start_date="2021-09-22",
            start_time="19:30",
            end_time="22:30",
            hours=32,
            sessions=4,
            workshops=2,
            cover="poster/devops-for-java-developers.jpg",
            temary="temary/devops-for-java-developers.pdf"
        ),
        Workshop(
            name="MICROSERVICES ARCHITECTURE JAVA, SPRING BOOT & SPRING CLOUD",
            description="Conceptualizaci??n, dise??o, programaci??n, pruebas y despliegue de microservicios utilizando Java con Spring Boot y Spring Cloud. Implementaci??n de principales patrones a trav??s de un caso pr??ctico evolutivo utilizando tecnol??gicas exclusivas. Adem??s de conocer las principales recomendaciones y buenas pr??cticas para implementar arquitecturas de microservicios a nivel empresarial.",
            price=899,
            level=[3],
            frequency=[3, 5],
            start_date="2021-09-29",
            start_time="19:30",
            end_time="22:00",
            hours=52,
            sessions=8,
            cover="poster/microservices-architecture-java-spring-boot-spring-cloud.jpg",
            temary="temary/microservices-architecture-java-spring-boot-spring-cloud.pdf"
        ),
        Workshop(
            name="FULL-STACK NET DEVELOPER ( NET 5 + ANGULAR 12 )",
            description="Parte Back-End: Desarrollo de la capa back-end utilizando NET 5, SQL Server 2019 y Visual Studio 2019. Se desarrollar?? un caso pr??ctico empresarial incluyendo pruebas, depuraci??n y monitoreo; incluyendo su consumo preliminar en Angular 12. Parte Front-End: Desarrollo de la capa front-end usando Angular 12, TypeScript y RxJS y Material Design. Se desarrollar?? un caso pr??ctico empresarial incluyendo pruebas, depuraci??n, monitoreo y despliegue.",
            price=899,
            level=[3],
            frequency=[6],
            start_date="2021-09-21",
            start_time="16:00",
            end_time="21:00",
            hours=52,
            sessions=8,
            cover="poster/full-stack-net-developer-net-5-angular-12.jpg",
            temary="temary/full-stack-net-developer-net-5-angular-12.pdf"
        ),
        Workshop(
            name="FULL-STACK REACTIVE DEVELOPER: SPRING WEBFLUX, REACT JS Y MONGODB",
            description="Implementaci??n y despliegue de Servicios Web RESTful utilizando Spring Boot, Spring WebFlux, Spring Data y Spring Security con MongoDB en Back-End y Aplicaciones Web utilizando React JS como Front-End, incluyendo pruebas (JUnit, Mockito, Postman y Jest), depuraci??n, monitoreo y despliegue.",
            price=899,
            level=[3],
            frequency=[6],
            start_date="2021-09-18",
            start_time="09:00",
            end_time="14:00",
            hours=52,
            sessions=8,
            cover="poster/full-stack-reactive-developer-spring-webflux-react-js-y-mongodb.jpg",
            temary="temary/full-stack-reactive-developer-spring-webflux-react-js-y-mongodb.pdf"
        ),
        Workshop(
            name="PROGRAMA DE ESPECIALIZACI??N: ASP.NET 5.0 DEVELOPER",
            description="Fundamentos de programaci??n: Conocer los fundamentos de programaci??n (codificaci??n, compilaci??n, c??digo fuente y ejecutable), historia, evoluci??n y tendencias de Net, ventajas y desventajas, mi primera aplicaci??n; tipos de datos, estructuras de control, excepciones, arreglos, colecciones, clases, interfaces, hilos, acceso a bases de datos, desarrollo de aplicaciones b??sicas. Aplicaciones ASP.NET 5.0: Contar con conocimientos y habilidades para iniciarse en el desarrollo de Aplicaciones Web con ASP.NET 5.0 y SQL Server. Aprender a aplicar principios y patrones b??sicos de dise??o de software, seguridad y despliegue. Proyecto de integraci??n: Contar con conocimientos y habilidades avanzadas en desarrollo de Aplicaciones Web con ASP.NET 5.0 y SQL Server. Aplicar principios y patrones avanzados de dise??o, seguridad, despliegue y buenas pr??cticas de desarrollo de software.",
            price=1259,
            level=[1, 2, 3],
            frequency=[3, 5],
            start_date="2021-08-20",
            start_time="19:30",
            end_time="22:00",
            hours=102,
            sessions=12,
            cover="poster/programa-especializacion-aspnet-50-developer.jpg",
            temary="temary/programa-especializacion-aspnet-50-developer.pdf"
        ),
        Workshop(
            name="19C ORACLE DATABASE TRACK SQL TUNING",
            description="El Track proporciona a los desarrolladores y administradores de bases de datos Oracle el conocimiento y la experiencia para realizar actividades de optimizaci??n de sentencias SQL en bases de datos Oracle. A trav??s de este curso aprender?? conceptos de optimizaci??n y su arquitectura con el fin de influir en ??l para optimizar las consultas. Se consideran sesiones te??ricas y ejercicios pr??cticos en el desarrollo de cada sesi??n.",
            price=499,
            level=[3],
            frequency=[7],
            start_date="2021-10-03",
            start_time="09:00",
            end_time="14:00",
            hours=26,
            sessions=4,
            cover="poster/19c-oracle-database-track-sql-tuning.jpg",
            temary="temary/19c-oracle-database-track-sql-tuning.pdf"
        ),
        Workshop(
            name="ESPECIALIZACI??N JAVA WEB DEVELOPER",
            description="Fundamentos de programaci??n Java: Conocer los fundamentos de programaci??n (codificaci??n, compilaci??n, c??digo fuente y ejecutable), historia, evoluci??n y tendencias de Java, ventajas y desventajas, mi primer programa; tipos de datos, estructuras de control, excepciones, Lambda Expressions, arreglos, colecciones, clases, interfaces, hilos, acceso a bases de datos, desarrollo de aplicaciones b??sicas de consola y escritorio. Aplicaciones Java Web: Desarrollo y despliegue de aplicaciones Web utilizando Java, JPA, JSF (PrimeFaces), JasperReport (iReport) y Apache POI. Se utilizar?? como motor de base de datos Oracle 18c (PL/SQL) y servidor de aplicaciones Apache Tomcat, JBoss y Web Logic. Servicios Web RestFul: Dise??o, implementaci??n y despliegue de servicios web empresariales basados en JAX-RS (Java API for RESTful Web Services), utilizando Spring Boot, Jersey y RESTEasy con Oracle y JPA/Hibernate/Spring Data. Su testeo se realizar?? v??a POSTMAN y JSONLint, su consumo se implementar?? a nivel de Java (incluye servicios externos).",
            price=1297,
            level=[1, 2, 3],
            frequency=[6],
            start_date="2021-09-25",
            start_time="16:00",
            end_time="21:00",
            hours=102,
            sessions=12,
            cover="poster/especializacion-java-web-developer.jpg",
            temary="temary/especializacion-java-web-developer.pdf"
        ),
        Workshop(
            name="Curso 1",
            description="Descripci??n del curso",
            price=500,
            level=[1, 2, 3],
            frequency=[6],
            start_date="2021-09-25",
            start_time="14:00",
            end_time="21:00",
            hours=102,
            sessions=12,
            cover="poster/especializacion-java-web-developer.jpg",
            temary="temary/especializacion-java-web-developer.pdf"
        ),
        Workshop(
            name="Curso 2",
            description="Descripci??n del curso",
            price=500,
            level=[1, 2, 3],
            frequency=[6],
            start_date="2021-09-25",
            start_time="16:00",
            end_time="21:00",
            hours=102,
            sessions=12,
            cover="poster/especializacion-java-web-developer.jpg",
            temary="temary/especializacion-java-web-developer.pdf"
        ),
        Workshop(
            name="Curso 3",
            description="Descripci??n del curso",
            price=500,
            level=[1, 2, 3],
            frequency=[6],
            start_date="2021-09-25",
            start_time="16:00",
            end_time="21:00",
            hours=102,
            sessions=12,
            cover="poster/especializacion-java-web-developer.jpg",
            temary="temary/especializacion-java-web-developer.pdf"
        ),
        Workshop(
            name="Curso 4",
            description="Descripci??n del curso",
            price=500,
            level=[1, 2, 3],
            frequency=[6],
            start_date="2021-09-25",
            start_time="16:00",
            end_time="21:00",
            hours=102,
            sessions=12,
            cover="poster/especializacion-java-web-developer.jpg",
            temary="temary/especializacion-java-web-developer.pdf"
        ),
        Workshop(
            name="Curso 5",
            description="Descripci??n del curso",
            price=500,
            level=[1, 2, 3],
            frequency=[6],
            start_date="2021-09-25",
            start_time="16:00",
            end_time="21:00",
            hours=102,
            sessions=12,
            cover="poster/especializacion-java-web-developer.jpg",
            temary="temary/especializacion-java-web-developer.pdf"
        ),
        Workshop(
            name="Curso 7",
            description="Descripci??n del curso",
            price=500,
            level=[1, 2, 3],
            frequency=[6],
            start_date="2021-09-25",
            start_time="16:00",
            end_time="21:00",
            hours=102,
            sessions=12,
            cover="poster/especializacion-java-web-developer.jpg",
            temary="temary/especializacion-java-web-developer.pdf"
        ),
        Workshop(
            name="Curso 8",
            description="Descripci??n del curso",
            price=500,
            level=[1, 2, 3],
            frequency=[6],
            start_date="2021-09-25",
            start_time="16:00",
            end_time="21:00",
            hours=102,
            sessions=12,
            cover="poster/especializacion-java-web-developer.jpg",
            temary="temary/especializacion-java-web-developer.pdf"
        ),
        Workshop(
            name="Curso 9",
            description="Descripci??n del curso",
            price=500,
            level=[1, 2, 3],
            frequency=[6],
            start_date="2021-09-25",
            start_time="16:00",
            end_time="21:00",
            hours=102,
            sessions=12,
            cover="poster/especializacion-java-web-developer.jpg",
            temary="temary/especializacion-java-web-developer.pdf"
        ),
        Workshop(
            name="Curso 10",
            description="Descripci??n del curso",
            price=500,
            level=[1, 2, 3],
            frequency=[6],
            start_date="2021-09-25",
            start_time="16:00",
            end_time="21:00",
            hours=102,
            sessions=12,
            cover="poster/especializacion-java-web-developer.jpg",
            temary="temary/especializacion-java-web-developer.pdf"
        ),
        Workshop(
            name="Curso 11",
            description="Descripci??n del curso",
            price=500,
            level=[1, 2, 3],
            frequency=[6],
            start_date="2021-09-25",
            start_time="16:00",
            end_time="21:00",
            hours=102,
            sessions=12,
            cover="poster/especializacion-java-web-developer.jpg",
            temary="temary/especializacion-java-web-developer.pdf"
        ),

    ])

    return Response({"message": "database populated"})



