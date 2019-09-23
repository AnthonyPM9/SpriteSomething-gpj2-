import distutils.dir_util			# for copying trees
import os											# for env vars
from shutil import copy, make_archive, move, rmtree	# file manipulation

# make dir to put app icon in
checkdir = "../pages/resources/app/meta/icons/"
if not os.path.isdir(checkdir):
	os.makedirs(checkdir)
# copy icon over
copy(
	"./resources/app/meta/icons/app.gif",
	"../pages/resources/app/meta/icons"
)

# make dir to put build version in
checkdir = "../pages/resources/app/meta/manifests/"
if not os.path.isdir(checkdir):
	os.makedirs(checkdir)
# copy app_version over
copy(
	"../build/app_version.txt",
	"../pages/resources/app/meta/manifests"
)
# copy badges manifest over
copy(
	"./resources/app/meta/manifests/badges.json",
	"../pages/resources/app/meta/manifests"
)

# copy GitHub Pages files to staging area
# copy index page
copy(
	"./pages_resources/index.html",
	"../pages"
)

# copy sprite previews
distutils.dir_util.copy_tree(
	"./pages_resources",
	"../pages/resources/app"
)

checkdir = "./resources/app"
for item in os.listdir(checkdir):
	if os.path.isdir(os.path.join(checkdir,item)):
		if not item == "meta":
			game = item
			gamedir = "../pages/resources/app/" + game
			if not os.path.isdir(gamedir + "/manifests/"):
				os.makedirs(gamedir + "/manifests/")
			distutils.dir_util.copy_tree(
				"./resources/app/" + game + "/manifests/",
				gamedir + "/manifests/"
			)
			distutils.dir_util.copy_tree(
				"./resources/app/" + game + "/lang/",
				gamedir + "/lang/"
			)
