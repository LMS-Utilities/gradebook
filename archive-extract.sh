sudo apt install p7zip-full

for f in *.zip
    do 7z x "$f" -o"${f%*.zip}"
done

for f in *.7z
    do 7z x "$f" -o"${f%*.7z}"
done


