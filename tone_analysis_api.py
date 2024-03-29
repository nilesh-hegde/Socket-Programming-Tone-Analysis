from watson_developer_cloud import ToneAnalyzerV3
import json

def cl_ana(text):
    tone_analyzer = ToneAnalyzerV3(version='********',username='****************',password='********************', url='https://gateway.watsonplatform.net/tone-analyzer/api')
    tone_analysis = tone_analyzer.tone({'text': text},'application/json').get_result()
    a1=tone_analysis['document_tone']
    a2=a1['tones']
    i=0
    while i<len(a2):
        a3=a2[i]
        if a3['tone_id']=='anger':
            return 1
        i=i+1
    return 0
