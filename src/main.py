from voice.voice_input_config import VoiceInputConfig
from voice.voice_input import VoiceInput
from voice.voice_output import VoiceOutput
from answer_api.wolfram_alpha import WolframAlpha
from config.config import Config
from audio.mp3 import Mp3




read_config = Config("../config/config")

voice_input = VoiceInput(read_config.get_speech_to_text_file())
voice_output = VoiceOutput(read_config.get_text_to_speech_file())
wolfram_alpha = WolframAlpha(read_config.get_wolfram_alpha_api_key())
mp3 = Mp3(read_config.get_text_to_speech_file())

speech_text = voice_input.get_speech()
wolfram_alpha.get(speech_text)
result_text = wolfram_alpha.parse()

if result_text is not None:
	voice_output.write_speech(result_text)
	mp3.play()
else:
	print("No answer available")

