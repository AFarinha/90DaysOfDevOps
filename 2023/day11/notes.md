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


#### Task 2
git switch -c development
cat version01.txt
cat > version01.txt << EOF
This is the bug fix in development branch
EOF
cat version01.txt
git add .
git commit -m "version01.txt updated"
git push origin development
git branch
echo "After bug fixing, this is the new feature with minor alteration" >> version01.txt
git add version01.txt
git commit -m "Added feature2.1 in development branch"
echo "This is the advancement of previous feature" >> version01.txt
git add version01.txt
git commit -m "Added feature2.2 in development branch"
echo "Feature 2 is completed and ready for release" >> version01.txt
git add version01.txt
git commit -m "Feature2 completed"
cat version01.txt
git log --oneline
cat version01.txt
git push
git push origin development
git switch master
git pull
git switch -c production
git rebase development
git log --oneline --graph --all --decorate
cat version01.txt
git push -u origin development
git push -u origin production

#### Task 3
git switch production
cat version01.txt
nano version01.txt
git cherry-pick e76355c
git add .
git cherry-pick --continue
echo "Added few more changes to make it more optimized." >> version01.txt
git add .
git commit -m "Optimized the feature"
cat version01.txt
git push