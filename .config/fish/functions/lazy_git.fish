function lazygit --description "Git add, git commit and push in one command"
	git add .
	git commit -m $argv
	git push
end
