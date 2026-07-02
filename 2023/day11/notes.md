#### Task 1
git switch master
git status
git switch -c stash-demo
echo "This change was created in stash-demo branch." > stash-demo.txt
git branch
git add stash-demo.txt
git stash push -m "Save changes from stash-demo branch"
git stash list
git status
git switch master
git switch -c stash-target
echo "This change was committed before applying stash." > stash-target.txt
git add stash-target.txt
git commit -m "Add committed change before stash pop"
git stash pop
git status
ls
cat stash-demo.txt
git add stash-demo.txt
git commit -m "Apply stashed changes"
git push -u origin stash-target
git push
git branch -d stash-target
git branch -d stash-demo
git branch