Update!
CSV files are now updated to include the new megas and their abilities along with any other random moves that were missing. Up to date with pokemon showdown server as of 6/20/2026.
------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

SetGenerator:

This has only been tested on Windows. The .exe only works on windows, so if you want to do this on another system, you'll need use the python code included.

Relatively simple to use. You need to fill in each of the required spots.

Validate button just checks to make sure everything is ok. Fields automatically update when you focus on something else, but the button is there just in case.

Pokémon: Name of the Pokémon, do not use any spaces or punctuation, and all lowercase

Moves: Include at least 1 move. All lowercase, include spaces and hyphens, nothing else

Item: Must include an item. All lowercase, include spaces and hyphens, nothing else.

Ability: Must include an ability. All lowercase, include spaces and hyphens, nothing else.

Tera type: must include a tera type. All lowercase

Output File: Included is "sets.json" this should be the file that you type in here.

Level: This isn't normally required. However, if the Pokémon your adding isn't already in "sets.json", then you need to include a level.

Add Pokémon button: does exactly what it says, it adds the Pokémon! Fun!

*Known Bug: Adding a new pokemon will create a key in the json file labeled "sets". I don't really know why this happens, but don't worry about it. It gets removed when using the file combiner

--------------------------------------------------------------------------------------

Once you've added all the Pokémon you want, you'll need to use file combiner.

Simply include up to 4 json files that you want to combine. Then click the big button. This will combine the json files and clean them of any sets that don't exist. cmd should output each pokemon being cycled through, so if there is an error, you can check the json file where it ended and that should help you identify the problem.

This will give you an output file called "combinedsets.json". Replace the sets.json file that you are replacing (typically either just "sets.json" or "doubles-sets.json") with this file (make sure to rename it so that it matches what you replaced).

You'll also need to edit the "teams.ts" file. To do this, just look for the code that deals with giving items, this is usually:
getItem()
getPriorityItem()
getDoublesItem()

Just delete everything from these functions after the first squiggly bracket ( { ) and replace it with: "return role"
without the quotation marks. Example:
override getItem(
		ability: string,
		types: string[],
		moves: Set<string>,
		counter: MoveCounter,
		teamDetails: RandomTeamsTypes.TeamDetails,
		species: Species,
		isLead: boolean,
		teraType: string,
		role: RandomTeamsTypes.Role,
	) {
		return role
	}


Link to youtube tutorial: https://youtu.be/miCD6MCol7w

--------------------------------------------------------------------------------------

Tips:

1) The included CSV files show how to input names. If you are unsure, consult them.

2) Don't be afraid of the json file. If you download something like visual studio code, you can open the json file with that and format the file using alt+shift+f and you can easily look through it. This lets you fix any mistakes in sets you've made.

3) If you're looking at my python code, I'm very sorry. It's not even remotely optimal. I managed to get it to work, and that's really all I needed. Please feel free to let me know if there are improvements that you think I should make.
