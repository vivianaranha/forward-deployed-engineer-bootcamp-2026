DISCOVERY_AREAS=("business_outcome","users","workflow","systems","data","constraints","risks","success_metrics")
def completeness(notes):
    return round(sum(bool(notes.get(k)) for k in DISCOVERY_AREAS)/len(DISCOVERY_AREAS),2)
