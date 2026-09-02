from django.db import models



class Informacion():
    def __init__(self, nombre, resumen, descripcion, caracteristica, precio, duracion):
        self.nombre = nombre
        self.resumen = resumen
        self.descripcion = descripcion
        self.caracteristica = caracteristica
        self.precio = precio
        self.duracion = duracion


def mostrarInformacion():
    servicios = {
        'desarrollo':[
            {
                'nombre'         :'Desarrollo de Sitios Web',
                'resumen'        :'Sitios y aplicaciones web a medida, rápidos y responsivos para tu negocio.',
                'descripcion'    : 'Diseñamos y desarrollamos sitios web y aplicaciones a medida para empresas que necesitan presencia digital profesional. Trabajamos con tecnologías modernas del lado del servidor para que tu sitio sea rápido, seguro y fácil de mantener.',
                'caracteristica' :[
                    'Diseño responsivo para escritorio, tablet y móvil',
                    'Panel de administración de contenidos,'
                    'Optimización de velocidad de carga',
                    'Integración con redes sociales y formularios de contacto'
                ],
                'precio'         : 450.000,
                'duracion'       :'3 a 6 semanas'
            }
        ],
        'consultoria':[
            {
                'nombre'         :'Consultoría en la Nube',
                'resumen'        :'Migración y optimización de infraestructura en la nube para tu empresa.',
                'descripcion'    : 'Ayudamos a tu empresa a migrar y optimizar su infraestructura en servicios en la nube, reduciendo costos operativos y mejorando la disponibilidad de tus sistemas críticos.',
                'caracteristica' :[
                    'Diagnóstico de infraestructura actual',
                    'Migración de servidores y bases de datos'
                    'Configuración de respaldos automáticos',
                    'Monitoreo y alertas 24/7'
                ],
                'precio'         : 600.000,
                'duracion'       :'2 a 4 semanas'
            }
        ],
        'aplicacion':[
            {
                'nombre'         :'Aplicaciones Móviles',
                'resumen'        :'Apps nativas e híbridas para Android e iOS, conectadas a tus sistemas.',
                'descripcion'    : 'Desarrollamos aplicaciones móviles para Android e iOS conectadas a tus sistemas de backend existentes, pensadas para acompañar a tus clientes desde el celular con la misma calidad que tu plataforma web.',
                'caracteristica' :[
                    'Apps nativas e híbridas (Android / iOS)',
                    'Notificaciones push y geolocalización'
                    'Conexión a API REST propia o de terceros',
                    'Publicación en Google Play y App Store'
                ],
                'precio'         : '890.000',
                'duracion'       :'6 a 10 semanas'
            }            
        ],
        'ciberseguridad':[
            {
                'nombre'         :'Ciberseguridad para Pymes',
                'resumen'        :'Protege los datos de tu empresa y de tus clientes con buenas prácticas reales.',
                'descripcion'    : 'Evaluamos la seguridad de tus sistemas y aplicamos buenas prácticas de protección de datos, control de accesos y respuesta ante incidentes, adaptadas a la realidad de una pyme.',
                'caracteristica' :[
                    'Auditoría básica de vulnerabilidades',
                    'Políticas de contraseñas y control de accesos'
                    'Respaldo y recuperación ante incidentes',
                    'Capacitación al equipo interno'
                ],
                'precio'         : '350.000',
                'duracion'       :'2 a 3 semanas'
            }                    
        ],

    }
    return servicios


# Create your models here.
