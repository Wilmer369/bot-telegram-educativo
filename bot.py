import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

TOKEN = os.getenv('TOKEN')

# Configuración de logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# URLs para los comandos
URLS = {
    "bienvenida": "https://viosacademy-collab.github.io/vios-academy-web",
    
    # Simuladores de Química
    "simulador_quimica_1": "https://phet.colorado.edu/sims/html/build-an-atom/latest/build-an-atom_es.html",
    
    # Simuladores de Física
    "simulador_fisica_1": "https://phet.colorado.edu/sims/html/friction/latest/friction_es.html",
    "simulador_fisica_2": "https://phet.colorado.edu/sims/html/energy-skate-park-basics/latest/energy-skate-park-basics_es.html",
    "simulador_fisica_3": "https://phet.colorado.edu/sims/html/energy-skate-park/latest/energy-skate-park_es.html",
    
    # Simuladores de Electrónica
    "simulador_electronica_1": "https://phet.colorado.edu/sims/html/resistance-in-a-wire/latest/resistance-in-a-wire_es.html",
    "simulador_electronica_2": "https://phet.colorado.edu/sims/html/ohms-law/latest/ohms-law_es.html",
    "simulador_electronica_3": "https://phet.colorado.edu/sims/html/circuit-construction-kit-dc-virtual-lab/latest/circuit-construction-kit-dc-virtual-lab_es.html",
    "simulador_electronica_4": "https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_es.html",
    "simulador_electronica_5": "https://phet.colorado.edu/sims/html/balloons-and-static-electricity/latest/balloons-and-static-electricity_es.html",
    "simulador_electronica_6": "https://phet.colorado.edu/sims/html/john-travoltage/latest/john-travoltage_es.html",
    
    # Simuladores de Matemáticas
    "simulador_matematicas_1": "https://phet.colorado.edu/sims/html/fractions-mixed-numbers/latest/fractions-mixed-numbers_es.html",
    "simulador_matematicas_2": "https://phet.colorado.edu/sims/html/fractions-intro/latest/fractions-intro_es.html",
    "simulador_matematicas_3": "https://phet.colorado.edu/sims/html/build-a-fraction/latest/build-a-fraction_es.html",
    "simulador_matematicas_4": "https://phet.colorado.edu/sims/html/fractions-equality/latest/fractions-equality_es.html",
    "simulador_matematicas_5": "https://phet.colorado.edu/sims/html/fraction-matcher/latest/fraction-matcher_es.html",
    
    # Calculadoras
    "calculadora_1": "https://www-symbolab-com.translate.goog/calculator/math/scientific?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc",
    "calculadora_2": "https://www-symbolab-com.translate.goog/calculator/conversion/megabytes?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc",
    "calculadora_3": "https://www-symbolab-com.translate.goog/calculator/math/fraction?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc",
    "calculadora_4": "https://www-symbolab-com.translate.goog/cheat-sheets?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc#",
    "calculadora_5": "https://www-symbolab-com.translate.goog/graphing-calculator?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc",
    "calculadora_6": "https://www.inventable.eu/calculadoras"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando start - Muestra la descripción principal"""
    welcome_text = """
🔬 **BOT DE SIMULADORES Y CALCULADORAS EDUCATIVAS**

¡Bienvenido! Este bot te proporciona acceso a herramientas educativas interactivas.

📋 **Comandos disponibles:**
/bienvenida - Página de bienvenida (Landing Page)
/simuladores - Lista de simuladores educativos
/calculadores - Lista de calculadoras y herramientas

💡 **Características:**
• Simuladores de PhET Colorado
• Calculadoras científicas
• Herramientas de conversión
• Recursos educativos interactivos

🚀 *Escribe un comando para comenzar...*
    """
    await update.message.reply_text(welcome_text, parse_mode='Markdown')

async def bienvenida(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Abre la página de bienvenida (landing page)"""
    keyboard = [
        [InlineKeyboardButton("🌐 Abrir Landing Page", url=URLS["bienvenida"])]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "📖 **Página de Bienvenida**\n\n"
        "Haz clic en el botón para abrir nuestra página de bienvenida:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def simuladores(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Muestra la lista de simuladores organizados por categorías"""
    
    # Crear teclado inline con todas las categorías de simuladores
    keyboard = [
        [InlineKeyboardButton("🧪 QUÍMICA", callback_data="categoria_quimica")],
        [InlineKeyboardButton("⚛️ FÍSICA", callback_data="categoria_fisica")],
        [InlineKeyboardButton("🔌 ELECTRÓNICA", callback_data="categoria_electronica")],
        [InlineKeyboardButton("📐 MATEMÁTICAS", callback_data="categoria_matematicas")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🎮 **SIMULADORES EDUCATIVOS**\n\n"
        "Selecciona una categoría para ver los simuladores disponibles:\n\n"
        "• 🧪 **Química**: Modelos atómicos\n"
        "• ⚛️ **Física**: Movimiento, energía, fricción\n"
        "• 🔌 **Electrónica**: Circuitos, resistencia, ley de Ohm\n"
        "• 📐 **Matemáticas**: Fracciones y operaciones\n\n"
        "💡 *Todos los simuladores se abren dentro de Telegram*",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def calculadores(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Muestra la lista de calculadoras y herramientas"""
    
    # Teclado con todas las calculadoras
    keyboard = [
        [
            InlineKeyboardButton("🔢 Calculadora Científica", url=URLS["calculadora_1"]),
            InlineKeyboardButton("📊 Convertidor Unidades", url=URLS["calculadora_2"])
        ],
        [
            InlineKeyboardButton("➗ Calculadora Fracciones", url=URLS["calculadora_3"]),
            InlineKeyboardButton("📚 Hoja Trucos Álgebra", url=URLS["calculadora_4"])
        ],
        [
            InlineKeyboardButton("📈 Calculadora Gráfica", url=URLS["calculadora_5"]),
            InlineKeyboardButton("⚡ Calculadora Electrónica", url=URLS["calculadora_6"])
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🧮 **CALCULADORAS Y HERRAMIENTAS**\n\n"
        "Selecciona la calculadora que necesitas:\n\n"
        "• 🔢 **Calculadora Científica** - Operaciones avanzadas\n"
        "• 📊 **Convertidor de Unidades** - Conversiones diversas\n"
        "• ➗ **Calculadora de Fracciones** - Operaciones con fracciones\n"
        "• 📚 **Hoja de Trucos de Álgebra** - Fórmulas y referencia\n"
        "• 📈 **Calculadora Gráfica** - Representación gráfica\n"
        "• ⚡ **Calculadora Electrónica** - Especializada en electrónica\n\n"
        "💡 *Todas las calculadoras se abren dentro de Telegram*",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Maneja los callbacks de los botones inline"""
    query = update.callback_query
    await query.answer()
    
    callback_data = query.data
    
    if callback_data == "categoria_quimica":
        keyboard = [
            [InlineKeyboardButton("🧪 Construye un Átomo", url=URLS["simulador_quimica_1"])]
        ]
        text = "🧪 **SIMULADORES DE QUÍMICA**\n\nConstruye y explora modelos atómicos interactivos."
    
    elif callback_data == "categoria_fisica":
        keyboard = [
            [InlineKeyboardButton("⚡ Fricción", url=URLS["simulador_fisica_1"])],
            [InlineKeyboardButton("🎯 Energía Pista Patinaje (Intro)", url=URLS["simulador_fisica_2"])],
            [InlineKeyboardButton("🚀 Energía Pista Patinaje (Completo)", url=URLS["simulador_fisica_3"])]
        ]
        text = "⚛️ **SIMULADORES DE FÍSICA**\n\nExplora conceptos de movimiento, energía y fuerzas."
    
    elif callback_data == "categoria_electronica":
        keyboard = [
            [InlineKeyboardButton("🔋 Resistencia en un Alambre", url=URLS["simulador_electronica_1"])],
            [InlineKeyboardButton("⚡ Ley de Ohm", url=URLS["simulador_electronica_2"])],
            [InlineKeyboardButton("🔌 Kit Circuitos CD (Lab Virtual)", url=URLS["simulador_electronica_3"])],
            [InlineKeyboardButton("💡 Kit Circuitos CD", url=URLS["simulador_electronica_4"])],
            [InlineKeyboardButton("🎈 Globos y Electricidad Estática", url=URLS["simulador_electronica_5"])],
            [InlineKeyboardButton("👨‍🔬 Travoltaje", url=URLS["simulador_electronica_6"])]
        ]
        text = "🔌 **SIMULADORES DE ELECTRÓNICA**\n\nConstruye circuitos y experimenta con electricidad."
    
    elif callback_data == "categoria_matematicas":
        keyboard = [
            [InlineKeyboardButton("🔢 Fracciones: Números Mixtos", url=URLS["simulador_matematicas_1"])],
            [InlineKeyboardButton("📚 Fracciones: Introducción", url=URLS["simulador_matematicas_2"])],
            [InlineKeyboardButton("🧱 Construye una Fracción", url=URLS["simulador_matematicas_3"])],
            [InlineKeyboardButton("⚖️ Fracciones: Igualdades", url=URLS["simulador_matematicas_4"])],
            [InlineKeyboardButton("🎯 Parejas de Fracciones", url=URLS["simulador_matematicas_5"])]
        ]
        text = "📐 **SIMULADORES DE MATEMÁTICAS**\n\nAprende y practica operaciones con fracciones."
    
    else:
        return
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Maneja comandos no reconocidos"""
    await update.message.reply_text(
        "❌ Comando no reconocido. Usa /start para ver los comandos disponibles.\n\n"
        "📋 **Comandos válidos:**\n"
        "/start - Descripción principal\n"
        "/bienvenida - Página de bienvenida\n"
        "/simuladores - Simuladores educativos\n"
        "/calculadores - Calculadoras y herramientas",
        parse_mode='Markdown'
    )

def main() -> None:
    """Función principal para iniciar el bot"""
    # Verificar que el token esté configurado
    if not TOKEN:
        logger.error("❌ TOKEN no encontrado. Configura la variable de entorno TOKEN")
        return
    
    application = Application.builder().token(TOKEN).build()

    # Registrar comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("bienvenida", bienvenida))
    application.add_handler(CommandHandler("simuladores", simuladores))
    application.add_handler(CommandHandler("calculadores", calculadores))
    
    # Manejar callbacks de botones inline
    application.add_handler(CallbackQueryHandler(handle_callback))
    
    # Manejar comandos desconocidos (DEBE SER EL ÚLTIMO)
    application.add_handler(MessageHandler(filters.COMMAND, unknown_command))

    # Iniciar el bot
    logger.info("🤖 Bot iniciado correctamente")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()