Day 3 Task: Basic Linux Commands

Task: What is the linux command to

1. To view what's written in a file.
cat README.md

2. To change the access permissions of files.
chmod 777 README.md

3. To check which commands you have run till now.
history
history 10

4. To remove a directory/ Folder.
mkdir temp
rmdir temp

5. To create a fruits.txt file and to view the content.
touch fruits.txt
or
echo "fruits txt" > fruits.txt
cat fruits.txt

6. Add content in devops.txt (One in each line) - Apple, Mango, Banana, Cherry, Kiwi, Orange, Guava.
cat > devops.txt << EOF
Apple
Mango
Banana
Cherry
Kiwi
Orange
Guava
EOF

7. To Show only top three fruits from the file.
head -n 3 devops.txt

8. To Show only bottom three fruits from the file.
tail -n 3 devops.txt

9. To create another file Colors.txt and to view the content.
touch Colors.txt
cat Colors.txt

10. Add content in Colors.txt (One in each line) - Red, Pink, White, Black, Blue, Orange, Purple, Grey.
cat > Colors.txt << EOF
Red
Pink
White
Black
Blue
Orange
Purple
Grey
EOF

11. To find the difference between fruits.txt and Colors.txt file.
diff devops.txt Colors.txt

Reference: https://www.linkedin.com/pulse/linux-commands-devops-used-day-to-day-activit-chetan-/

[← Previous Day](../day02/README.md) | [Next Day →](../day04/README.md)
