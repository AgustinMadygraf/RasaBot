# Sistema Inteligente de Control de Calidad – Chatbot Informativo

Este repositorio describe el bot conversacional desarrollado para acompañar al **proyecto "Industria 4.0: Sistema Inteligente de Control de Calidad en la producción de bolsas de papel mediante IoT y decisiones basadas en datos"**. El proyecto busca modernizar la producción de bolsas en la cooperativa Madygraf mediante sensores y técnicas de análisis de datos. Con esta solución se pretende automatizar el control de tres instancias críticas del proceso (alineación de la bobina, entubado y doblado de la base), aumentar la disponibilidad y la velocidad de producción y reducir la cantidad de productos defectuosos.

## Objetivo del bot

El objetivo inicial del bot es **brindar información al público en general** acerca del proyecto FITBA, sus motivaciones y sus alcances. A medida que se despliegue el sistema en planta, se podrán añadir nuevas funcionalidades para operarios y supervisores. Algunas de las consultas que resuelve el bot son:

```
1. Explicar qué es FITBA y qué rol cumplen la UNPAZ y la cooperativa Madygraf.
2. Describir cómo se utilizan dispositivos IoT, tales como balanzas digitales y visión artificial, para monitorear variables de producción.
3. Exponer los beneficios esperados: mejora en la eficiencia global del equipo (OEE), reducción de paradas no programadas, disminución del desperdicio y trazabilidad de costos.
```

En esta primera versión el bot es **reactivo**. Responde a las preguntas que le hagan las personas usuarias en Telegram y no envía notificaciones de manera proactiva. Sin embargo, la arquitectura está preparada para añadir alertas automáticas en versiones futuras.

## Arquitectura y componentes

El bot está construido con Rasa, un framework en Python para procesamiento de lenguaje natural y gestión de diálogos. De manera resumida, la arquitectura comprende:

```
**Modelo de NLU:** define las intenciones y entidades que el bot debe reconocer (por ejemplo, preguntar_proyecto, consultar_tecnologias, pedir_beneficios). Se entrenan con ejemplos de frases que las personas usuarias pueden formular.
**Historias y reglas:** determinan cómo debe comportarse el bot en diferentes contextos. Para las consultas informativas se utilizan historias simples que devuelven texto explicativo.
**Acciones personalizadas:** permiten conectar el bot con fuentes de datos externas. En este proyecto ya existe una API que expone información de sensores y estadísticas; en futuras versiones, las acciones podrán consultarla para ofrecer datos en tiempo real.
**Conector de Telegram:** integra Rasa con el servicio de mensajería. Se configura mediante credentials.yml (no incluido aquí) para especificar el token del bot de Telegram.
```

## Instrucciones conceptuales para ejecución

```
**1. Instalación de dependencias:** Asegúrese de tener instalado Python 3.8 o superior y el paquete rasa. También se requiere una cuenta de bot en Telegram y el correspondiente token.
**2. Entrenamiento del modelo:** Organice las frases de ejemplo en ficheros de datos (data/) y ejecute el entrenamiento de Rasa para generar un modelo de diálogo. Esto crea un archivo en models/ que podrá ser cargado por el servidor.
*3. *Configuración de credenciales:** En un archivo credentials.yml se define el canal de Telegram con su token. Este archivo no se versiona para proteger la información sensible.
**4. Despliegue en la nube:** El bot se puede ejecutar en un servidor o servicio en la nube que soporte Python. Al iniciar, se carga el modelo entrenado y se conecta con Telegram para atender los mensajes. El proyecto FITBA ya cuenta con un entorno de despliegue configurado.
```

## Futuras ampliaciones
Las capacidades del bot se irán ampliando de forma incremental, en consonancia con la evolución del proyecto:

```
**Datos en tiempo real para el público interno:** las acciones personalizadas se podrán enlazar con la API de sensores para responder preguntas como «¿cómo está la alineación de la bobina?» o «¿cuál es el OEE de hoy?».
**Alertas proactivas:** se podrán configurar notificaciones automáticas cuando se detecten desvíos significativos o fallas en el sistema de control de calidad.
**Segmentación por roles:** se planea distinguir entre personas operarias, supervisores y público externo, ofreciendo respuestas adaptadas a cada perfil.
**Mejora continua del lenguaje:** conforme aumente el volumen de consultas, se ajustarán las intenciones y se ampliará el vocabulario para reflejar la jerga técnica de Madygraf.
```

## Referencias

El documento de fondo del proyecto está disponible como [docs/FITBA_UNPAZ-Madygraf_Resumen.md](docs/FITBA_UNPAZ-Madygraf_Resumen.md). En él se detalla el problema que se busca resolver, las tecnologías aplicadas y las experiencias de innovación previas de la cooperativa. Este bot se diseña para facilitar la difusión de dicha información y servir de puente con la comunidad.
