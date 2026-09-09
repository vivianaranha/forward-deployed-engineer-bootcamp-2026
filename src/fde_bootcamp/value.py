from dataclasses import dataclass
@dataclass
class WorkflowBaseline:
    tasks_per_month:int
    minutes_per_task:float
    labor_cost_per_hour:float
def monthly_labor_cost(x):
    return round(x.tasks_per_month*x.minutes_per_task/60*x.labor_cost_per_hour,2)
def monthly_savings(x,new_minutes_per_task):
    before=monthly_labor_cost(x)
    after=monthly_labor_cost(WorkflowBaseline(x.tasks_per_month,new_minutes_per_task,x.labor_cost_per_hour))
    return round(before-after,2)
def annualized_value(monthly_value): return round(monthly_value*12,2)
