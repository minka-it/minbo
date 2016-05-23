# -*- coding: utf-8 -*-
'''
Código generado por la Comunidad Minka-IT para el bot *minbo*.
TelegramBot: @MinkaITBot
BotName: minbo
'''

from py_expression_eval import Parser
import telebot, os, aiml, sys
reload(sys)
sys.setdefaultencoding('utf8')

bot = telebot.TeleBot("TOKEN")
parser = Parser()

# Cargar el kernel, setear valores y aprender conocimiento
kernel = aiml.Kernel()
kernel.setBotPredicate('name', 'Minbo')
kernel.setBotPredicate('nombre_bot', 'Minbo')
kernel.setBotPredicate('master', 'Ramiro Martinez')
kernel.setBotPredicate('botmaster', 'Ramiro')
kernel.setBotPredicate('ciudad', 'San Salvador de Jujuy')
kernel.setBotPredicate('edad', '1')
kernel.learn("aiml/sara/sara_srai_1.aiml")
kernel.learn("aiml/sara/sara_srai_2.aiml")
kernel.learn("aiml/sara/nombres.aiml")
kernel.learn("aiml/sara/default.aiml")
kernel.learn("aiml/sara/numeros.aiml")
kernel.learn("aiml/sara/sexo.aiml")
kernel.learn("aiml/sara/sara.aiml")

text_messages = {
    'bienvenido':
        'Bienvenid@, entusiasta {name}!\n\n'
        'Este grupo es para mantener a todos los miembros de la comunidad Minka-IT conectados.\n'
        'No dudes en plantear tus inquietudes aquí o en algunos de los canales de comunicación de Minka-IT!\n'
        'Esperamos que disfrutes de formar parte del grupo :)',

    'info':
        'Mi nombre es *minbo*,\n'
        'Soy el bot que te brindará información acerca de la comunidad Minka-IT.\n'
        'Estoy en etapa de desarrollo, no dudes en agregarme nuevas funcionalidades!\n'
        'Mi código se encuentra en GitHub! repositorio temporal: https://github.com/jorgex9/minka-it.git',

    'help_calc':
        'Uso\n'
        '/calc expr\n'
        '\n'
        'Operaciones disponibles, constantes y funciones\n'
        '\n'
        'Expression Ejemplo                                 Salida\n'
        "+           2 + 2       4.0\n"
        "-           3 - 1       2.0\n"
        "*           2 * 3       6.0\n"
        "/           5 / 2       2.5\n"
        "%           5 % 2       1.0\n"
        "^           5 ^ 2       25.0\n"
        "PI          PI          3.141592653589793\n"
        "E           E           2.718281828459045\n"
        "sin(x)      sin(0)      0.0\n"
        "cos(x)      cos(PI)     - 1.0\n"
        "tan(x)      tan(0)      0.0\n"
        "asin(x)     asin(0)     0.0\n"
        "acos(x)     acos(-1)    3.141592653589793\n"
        "atan(x)     atan(PI)    1.2626272556789118\n"
        "log(x)      log(1)      0.0\n"
        "abs(x)      abs(-1)     1.0\n"
        "ceil(x)     ceil(2.7)   3.0\n"
        "floor(x)    floor(2.7)  2.0\n"
        "round(x)    round(2.7)  3.0\n"
        "exp(x)      exp(2)      7.38905609893065\n",


    'help_chat':
        'Puedes hablar conmigo si estas aburrid@.\n'
        'Soy un Chaterbot basado en la base de conocimiento de SARA.\n'
        'Estoy implementado gracias a pyaiml.\n'
        'Mi creador es Ramiro Martinez y la comunidad Minka-IT.\n'
        'Proximamente mi creador me dotara de capacidad de aprendizaje en tiempo real.',

    'wrong_chat':
        'Hubo un error'
}

def listener(messages):
    for m in messages:
        chat_id = m.chat.id # Obtenemos el ID del chat (cada chat tiene uno único)
        texto = m.text      # y el texto que se nos ha enviado
#        print('ID: ' + str(chat_id) + ' MENSAJE: ' + texto) 
        print("Nuevo mensaje recibido") # Sólo un mensaje en consola para que avise cuando haya un nuevo msj

bot.set_update_listener(listener)

#@bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
@bot.message_handler(content_types=['new_chat_member'])
def on_user_joins(message):
    name = message.new_chat_member.first_name
    print name
    #if hasattr(message.new_chat_member, 'last_name') and message.new_chat_member.last_name is not None:
    if message.new_chat_member.last_name is not None:
        name += u" {}".format(message.new_chat_member.last_name)
        print "Nuevo miembro en el grupo"
        print name

    #if hasattr(message.new_chat_member, 'username') and message.new_chat_member.username is not None:
    if message.new_chat_member.username is not None:
        name += u" (@{})".format(message.new_chat_member.username)
        print "Nuevo miembro en el grupo"
        print name

    chat_id = message.chat.id
    bot.reply_to(message, text_messages['bienvenido'].format(name=name))
#    bot.send_message(chat_id, text_messages['bienvenido'].format(name=name))

@bot.message_handler(commands=['info', 'help'])
def on_info(message):
    chat_id = message.chat.id
    #bot.reply_to(message, text_messages['info']) # respondemos con el mensaje correspondiente a info que está en el diccionario
    bot.send_message(chat_id, text_messages['info']) # respondemos con el mensaje correspondiente a info que está en el diccionario

@bot.message_handler(commands=["ping"])
def on_ping(message):
    chat_id = message.chat.id
    #bot.reply_to(message, "Aquí estoy, vivito y coleando!")
    bot.send_message(chat_id, "Aquí estoy, vivito y coleando!")

@bot.message_handler(commands=['acercade'])
def send_acercade(message):
    #bot.reply_to(message, 'Somos la comunidad Minka-IT, un espacio formado por y para estudiantes de carreras informáticas\nde la Facultad de Ingeniería de la U.N.Ju. Aquí podrás plantear tus ideas, proyectos, compartir\ntu conocimiento y aprender cosas nuevas relacionadas con la informática.')
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Somos la comunidad Minka-IT, un espacio formado por y para estudiantes de carreras informáticas\nde la Facultad de Ingeniería de la U.N.Ju. Aquí podrás plantear tus ideas, proyectos, compartir\ntu conocimiento y aprender cosas nuevas relacionadas con la informática.')

@bot.message_handler(commands=['documentos'])
def send_documentos(message):
    chat_id = message.chat.id
    #bot.reply_to(message, "Aquí puedes encontrar los documentos de la comunidad Minka-IT:\n http://bit.ly/24bon1o")
    bot.send_message(chat_id, "Aquí puedes encontrar los documentos de la comunidad Minka-IT:\nhttp://bit.ly/24bon1o")

@bot.message_handler(commands=['canales'])
def send_documentos(message):
    chat_id = message.chat.id
    #bot.reply_to(message, "Minka en Facebook: http://bit.ly/1VGbO9g\nMinka en IRC: #minkait")
    bot.send_message(chat_id, "Minka en Facebook: http://bit.ly/1VGbO9g\nMinka en IRC: #minkait")

@bot.message_handler(commands=['calc'])
def calc(message):
    chat_id = message.chat.id
    param = message.text.split(' ',1) #separa el comando de los parametros  
    if len(param) == 1 or param[1]=="help":
        bot.send_message(chat_id,text_messages['help_calc'])
    else:
        try:    
            #bot.send_message(chat_id, ast.literal_eval(param[1]))
            bot.send_message(chat_id,parser.parse(param[1]).evaluate({}))
            print "calc handler sucess: " + param[1]
        except Exception as e:
            bot.send_message(chat_id, "¡¡No podes calcular eso!!")
            print "calc handler error: " + str(e) + ": " + param[1]

@bot.message_handler(commands=['chat','minbo'])
def chat(message):
    chat_id = message.chat.id
    param = message.text.split(' ',1) #separa el comando de los parametros
    if len(param) == 1 or param[1]=="help":
        bot.send_message(chat_id,text_messages['help_chat'])
    else:
        try:
            print "chat humano: " + param[1]
            respuesta=kernel.respond(param[1])
            print "chat robot: " + respuesta
            bot.send_message(chat_id,respuesta)
        except Exception, e:
            print e
            bot.send_message(chat_id,"Tengo un bug en mi estomago!")

bot.polling(none_stop=True)       # Iniciamos nuestro bot para que esté atento a los mensajes
