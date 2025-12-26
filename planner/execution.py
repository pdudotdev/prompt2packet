def build_execution_plan(intent):
    return {
        "protocol": intent.protocol,
        "template": intent.model_dump(exclude={"count", "interval_ms"}),
        "count": intent.count,
        "interval_ms": intent.interval_ms,
    }
