

if [[ $# -ne 1 ]]
then
    echo "Usage: $0 <day_number>"
    exit 1
fi


DAY=$(printf "%02d" $1)

if test -f "day_$DAY.py"; then
    echo "day_$DAY.py exists."
else
  cp "template.py" "day_$DAY.py"
fi

touch "in/day_${DAY}_small.txt"
touch "in/day_${DAY}.txt"






