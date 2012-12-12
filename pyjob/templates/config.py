


from pyjob.parameter import Choices, Range

grid_params = {'alpha': Range(0.,1.1,0.1), 
               'show': Choices(['BFMTV_BFMStory',
                                'BFMTV_PlaneteShowbiz',
                                'LCP_CaVousRegarde',
                                'LCP_EntreLesLignes',
                                'LCP_LCPInfo13h30',
                                'LCP_LCPInfo20h30',
                                'LCP_PileEtFace',
                                'LCP_TopQuestions'])
               }

qsub_params = {'queue': '48giga.q',
               'job_name': 'ss.D',
               'concurrent_jobs': 20,
               'threads': 12,
               }
