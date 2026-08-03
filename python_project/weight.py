workout_records = [
    {
        "date": "2026-08-01",
        "exercise": "벤치프레스",
        "body_part": "가슴",
        "weight": 100,
        "reps": 5,
        "sets": 3
    },
    {
        "date": "2026-08-01",
        "exercise": "스쿼트",
        "body_part": "하체",
        "weight": 150,
        "reps": 5,
        "sets": 3
    },
    {
        "date": "2026-08-02",
        "exercise": "벤치프레스",
        "body_part": "가슴",
        "weight": 102.5,
        "reps": 4,
        "sets": 3
    }
]

for workout in workout_records:
    volume = workout["weight"] * workout["reps"] * workout["sets"]

    print(
        workout["date"],
        workout["exercise"],
        f"{volume}kg"
    )