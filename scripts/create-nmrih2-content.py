from pathlib import Path

root = Path('src/content/wiki')
for locale in ('en', 'vi', 'de', 'fr', 'es'):
    (root / locale / 'guides').mkdir(parents=True, exist_ok=True)
(root / 'en' / 'home').mkdir(parents=True, exist_ok=True)

pages = {
    'weapons': (
        'No More Room in Hell 2 Weapons Guide',
        'No More Room in Hell 2 weapons guide covering firearms, melee categories, attachments, ammunition handling, and practical 1.0 launch reference notes.',
        '/images/3.webp',
        'Weapons Guide',
        'Firearms, melee weapons, and attachments all serve a different job in an extraction run. The supplied 1.0 launch material supports learning categories and handling habits before treating any roster as complete.',
        ['Weapon Wiki: confirmed reference|An early official count in the supplied material lists 15 firearms, 19 melee weapons, and several tools. That is an early count rather than a verified complete 1.0 inventory. A reference list includes M9A3, M1911, MP5, Rochester 1873, Hunter 85, M14, M7A1, MC-15, and 590A1.', 'Firearms Guide: noise and ammunition|Gunfire can pull more zombies toward a fight, so a firearm is not only a damage decision. Save ammunition for threats that cannot be safely routed around or controlled with melee. Hold U to unload a weapon and recover its rounds when changing plans; this control is from player testing at the 1.0 launch.', 'Melee Guide: blunt and edged roles|The supplied references divide melee weapons into Blunt and Edged categories and note charged attacks. Use melee where space, stamina, and nearby enemies make it safer than a loud shot. No supplied source provides a complete current damage table.', 'Attachment Guide|Player launch reference identifies sights, suppressors, and flashlights. Incompatible attachments cannot be fitted. Suppressors are not silent: they reduce the distance at which shots attract zombies, but do not remove the need for positioning.', '1.0 limits|Combat, melee, firearms, and ammunition received broad 1.0 balancing. The Fandom inventory may be outdated and does not document full 1.0 statistics.'],
        ['/weapons-tier-list', '/tips', '/perks']),
    'weapons-tier-list': (
        'NMRIH2 Weapons Tier List',
        'NMRIH2 community weapons tier list based on 1.0 gameplay, covering M781, MP5, M1911, M14, 590A1, baseball bat, and fire axe context.',
        '/images/3.webp', 'Weapons Tier List',
        'This is a community tier list based on 1.0 gameplay, not an official ranking. It records one creator’s launch-period tests and should guide discussion rather than replace squad testing.',
        ['Community Tier List Guide|The supplied ranged ranking puts the M781 in S tier. The creator cites full-auto fire, attachment support, a 20-round magazine, and reported headshot performance as reasons to prioritize it for solo or co-op play.', 'A Tier Weapons Wiki|The M14 Battle Rifle, MP5, MC-15, M1911, and 590A1 appear in A tier. The MP5 is presented as versatile for crowd control. M1911 is the highest-ranked handgun, while the 590A1 is favored for close range.', 'B and C Tier Guide|Rochester 1873 and Hunter 85 are placed in B because high damage is offset by slow reloads and small magazines. Model 13, Ferrera DB12, and M93A3 are placed in C because capacity or reload limits narrow their role.', 'Melee Tier List: version note|The supplied melee ranking puts the baseball bat first and the fire axe among preferred melee options. It is an EA community ranking; as of 1.0 launch, may differ.', 'Choose for role, not letters|The creator recommends M1911 or M14 for ammunition-efficient solo play, while MP5, 590A1, and M781 fit close team protection and horde control.'],
        ['/weapons', '/tips', '/perks']),
    'perks': (
        'NMRIH2 Perks Guide',
        'NMRIH2 perks guide for Armageddon 1.0: reloading additions, removed perks, observed launch-day skills, three-choice upgrades, and reroll context.',
        '/images/1.jpg', 'Perks Guide',
        'Perks shape each Responder’s role. Armageddon 1.0 changed the pool, while the detailed effect list in the supplied material is launch-day player observation rather than an official complete database.',
        ['1.0 Perk Changes Guide|Armageddon added Handgun Reloading, Rifle Reloading, and Shotgun Reloading. It removed Averaging, Guts, and Teddy Bear, and lowered perk reroll cost.', 'Level-Up Choices Wiki|Player testing at the 1.0 launch reports one choice from three perks at level-up. Each pick is a role decision: ammunition, recoil, stamina, carry capacity, revives, and weapon handling can matter more than raw damage.', 'Observed Perks Guide|Observed names include Heavy Rifles, Dismember, Steady Shot, Two-Handed Melee, Hipfire Accuracy, One-Handed Melee, Environmental, Mule, Handgun Limb, Handgun Spread, Kicks, Staying Alive, Scavenger, Shotgun Range, and Handgun Reload.', 'Build around the squad|Mule helps a scavenger carry more, Staying Alive is described as faster revives, and Scavenger as greatly increased ammunition pickup. These descriptions are launch-day player observations.', 'What is not confirmed|The material lacks exact modifiers, complete pool weighting, unlock rules, final reroll prices, and a definitive level-cap table.'],
        ['/characters', '/weapons', '/tips']),
    'characters': (
        'NMRIH2 Characters and Responders Guide',
        'NMRIH2 characters guide explaining Responders, backgrounds, independent progression, customization, named starting Responders, Rescue Beacon, and permadeath context.',
        '/images/1.jpg', 'Characters Guide',
        'Players control Responders rather than fixed combat classes. Each Responder carries independent progression and can be permanently lost, so a character is both a build and a run-level risk.',
        ['Responder Wiki|Responders are not fixed heroes with a permanent combat role. Their independent levels and perk choices let characters develop differently, while death can remove the Responder from the roster.', 'Starting Characters Guide|A launch-day player stream observed Crackle, Bluff, and Twilight as three starting Responders. The same source says backgrounds influence starting skills and cites Bluff’s Bear Hunter background.', 'Customization and progression|Armageddon expanded appearance, clothing, compass, flashlight, and voice options. Player observation also describes hair, skin tone, eye color, clothing, and some Credit-gated cosmetics.', 'Permadeath and Rescue Beacon|A dead Responder is normally a permanent loss. Armageddon introduced Rescue Beacon, a consumable loadout item described as preventing one character death while losing the loadout.', 'Plan the roster|Create multiple Responders for different roles, but do not mistake that for disposable progression. Decide early when extraction is safer than a risky objective.'],
        ['/perks', '/solo', '/infection']),
    'maps': (
        'NMRIH2 Maps Guide',
        'NMRIH2 maps guide to six Objective maps, three Survival maps, Raven Rock, and a player-observed Broadway objective route for the 1.0 launch.',
        '/images/2.webp', 'Maps Guide',
        'No More Room in Hell 2 has six Objective maps and three Survival maps in the supplied 1.0 material. Learn a map’s objective flow before treating routes or loot as fixed.',
        ['Objective Maps Wiki|The six Objective maps listed in the supplied material are Lewiston, Power Plant, Pottsville, Broadway, Beaulieu Hospital, and Raven Rock. Raven Rock is the sixth Objective map and a 1.0 addition set around an underground military installation.', 'Survival Maps Guide|Flooded, Lighthouse, and Night of the Living Dead are the three Survival maps listed for 1.0. The supplied material does not provide full layouts, loot maps, or objective pools for these locations.', 'Broadway Walkthrough Reference|A player’s solo run records a possible Broadway sequence: restore generator power, tune a radio, locate and upload hard-drive data three times, pass CRC safehouses, travel through the subway, then extract.', 'Broadway Extraction Guide|The same run records two endings: fuel a signal bonfire and wait for a helicopter, or obtain keys, clear tracks, restore power, and leave by train. Objective randomization may produce variants.', 'Learn safely first|Solo Training is the sensible place to learn landmarks, objectives, and exits without normal progression or permanent character loss.'],
        ['/survival-mode', '/solo', '/tips']),
    'survival-mode': (
        'NMRIH2 Survival Mode Guide',
        'NMRIH2 Survival Mode guide covering Speakers, five-minute waves, three-wave helicopter extraction, early extraction notes, and Flooded, Lighthouse, and Night maps.',
        '/images/4.webp', 'Survival Mode',
        'Survival Mode is Armageddon 1.0’s second mode: a squad protects Speakers that attract zombies, survives waves, and extracts by helicopter after the recorded objective sequence.',
        ['Survival Mode Wiki|Survival Mode arrived with Armageddon 1.0 as a second play mode alongside Objective runs. The supplied material describes protecting Speakers that attract zombies.', 'Wave and Extraction Guide|Each wave is described as lasting five minutes. After three waves, the team can extract by helicopter. The same summary says a team that fails two waves can extract early.', 'Survival Maps Guide|Flooded, Lighthouse, and Night of the Living Dead are the three dedicated Survival maps. A player review characterizes the mode as defending three areas against three waves.', 'Squad Planning|Protect the objective, keep sight lines usable, and reserve ammunition for pressure points. Exact enemy compositions, rewards, Speaker placements, and difficulty scaling are not supplied.', 'Practice before progression|Solo Training supports practice on Objective and Survival maps without normal progression or permanent character loss.'],
        ['/maps', '/solo', '/tips']),
    'solo': (
        'NMRIH2 Solo Training Guide',
        'NMRIH2 Solo Training guide explaining the 1.0 practice mode, Objective and Survival map learning, local sessions, no normal progression, and no permadeath risk.',
        '/images/2.webp', 'Solo Training',
        'Solo Training is a 1.0 practice space, not a full solo campaign. It lets a player learn maps, objectives, and weapons without normal progression or permanent Responder loss.',
        ['Solo Training Wiki|Solo Training was added with Armageddon 1.0. It is designed for map learning, objective practice, and weapon familiarization rather than ordinary progression.', 'What you can practice|A player review reports that Objective and Survival maps can both be practiced alone. It is useful for checking routes, landmarks, basic combat handling, and movement.', 'What does not carry over|Solo Training has no normal progression and no character permadeath risk. It is not a way to farm the ordinary multiplayer economy or build a permanent solo campaign character.', 'Use a practice plan|Pick one question for a session: find an exit, learn an objective chain, test a weapon role, or rehearse navigation.', 'From practice to co-op|Once the map is familiar, join a team and communicate the route, resources, and extraction plan.'],
        ['/maps', '/survival-mode', '/tips']),
}

def write(locale, slug, title, description, image, label, summary, sections, links):
    body = [f'![No More Room in Hell 2 {label} reference]({image})', '']
    for section in sections:
        heading, text = section.split('|', 1)
        body.extend([f'## {heading}', text, ''])
    body.extend(['## Related Articles', *[f'- [Read Guide]({link})' for link in links]])
    text = f'''---\ntitle: "{title}"\ndescription: "{description}"\ncategory: guides\ndate: 2026-08-15\nlastModified: 2026-08-15\nimage: {image}\ntags: ["nmrih2", "{slug}", "guide"]\nsummary: "{summary}"\nauthor: "NMRIH2 Wiki"\n---\n\n''' + '\n'.join(body) + '\n'
    (root / locale / 'guides' / f'{slug}.mdx').write_text(text, encoding='utf-8')

for slug, entry in pages.items():
    write('en', slug, *entry)
