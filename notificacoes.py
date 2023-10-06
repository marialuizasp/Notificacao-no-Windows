from winotify import Notification, audio

notificacao = Notification(app_id="Codigo Pyton", title="Notificação da automação",
                           msg="Escreva a mensagem aqui",
                           duration="short", icon=r"C://Users/Maria Luiza/Downloads/twitter.png")

notificacao.set_audio(audio.LoopingAlarm, loop=False)
notificacao.add_actions(label="Nome do botão", launch="https://twitter.com/")

notificacao.show()