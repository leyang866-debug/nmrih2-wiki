from pathlib import Path
metadata = {
 'tips': ('NMRIH2 Tips Guide for New Players','NMRIH2 new-player tips for squad positioning, noise, inventory, ammunition, doors, navigation, infection awareness, and 1.0 player reference notes.','/images/3.webp','Stay with the main squad, reduce avoidable noise, share supplies, and choose extraction before a fight drains the team’s resources.'),
 'infection': ('NMRIH2 Infection Guide','NMRIH2 infection guide covering player-observed symptoms, pills, Gene Therapy, squad communication, prevention context, and an Early Access version warning.','/images/4.webp','Infection is a core risk alongside extraction and permanent character loss, so communicate observed symptoms and treatment needs to the squad early.'),
 'crossplay': ('NMRIH2 Crossplay Guide','NMRIH2 crossplay guide for PC, PS5, and Xbox Series X|S, covering platform interoperability, eight-player co-op context, and unsupported assumptions.','/images/1.jpg','No More Room in Hell 2 supports full crossplay across PC, PS5, and Xbox Series X|S at the 1.0 launch.'),
 'ps5': ('NMRIH2 PS5 Guide','NMRIH2 PS5 guide covering the 2026-08-11 console launch, $29.99 reference price, crossplay, 60 FPS target context, and support limits.','/images/5.jpg','No More Room in Hell 2 launched on PS5 with Armageddon 1.0, crossplay, and a supplied $29.99 US launch price reference.'),
 'xbox': ('NMRIH2 Xbox Guide','NMRIH2 Xbox guide for Xbox Series X|S covering 1.0 launch, $29.99 reference price, Play Anywhere, multiplayer subscription, and crossplay.','/images/5.jpg','No More Room in Hell 2 supports Xbox Series X|S with 1.0 console launch, crossplay, and supplied online multiplayer context.'),
 'review': ('NMRIH2 Review: 1.0 Launch Status','NMRIH2 review covering the 1.0 launch status, Mixed Steam reception snapshot, Early Access concerns, an 8/10 player reference, and console issues.','/images/4.webp','The supplied 2026-08-15 snapshot records Mixed Steam reception, alongside launch-period player discussion of Armageddon 1.0.'),
 'release-date': ('NMRIH2 Release Date Guide','NMRIH2 release date guide: Early Access began 2024-10-22, Armageddon 1.0 launched 2026-08-11, and PS5/Xbox released with 1.0.','/images/5.jpg','No More Room in Hell 2 entered Early Access on 2024-10-22 and released Armageddon 1.0 on 2026-08-11.'),
 '1.0-update': ('NMRIH2 Armageddon 1.0 Update Guide','NMRIH2 Armageddon 1.0 update guide for Survival Mode, Raven Rock, Solo Training, tutorial, consoles, crossplay, perks, and difficulty changes.','/images/5.jpg','Armageddon 1.0 released on 2026-08-11 and moved No More Room in Hell 2 out of Early Access with modes, maps, and systems.'),
 'difficulty': ('NMRIH2 Difficulty Levels Guide','NMRIH2 difficulty guide for Beginner, Normal, Hard, and Nightmare, including sourced 1.0 distinctions, rewards context, and limits on exact values.','/images/4.webp','No More Room in Hell 2 has Beginner, Normal, Hard, and Nightmare levels; supplied material supports broad differences, not a full numeric table.'),
 'steam-charts': ('NMRIH2 Steam Charts Guide','NMRIH2 Steam charts guide covering the 11K Early Access peak, 2026 pre-1.0 records, ownership estimates, and why live player counts stay external.','/images/1.jpg','Steam counts change continuously, so this guide does not hard-code a live number and instead records supplied historical Steam-only context.'),
}
for slug,(title,desc,image,summary) in metadata.items():
 p=Path('src/content/wiki/en/guides') / f'{slug}.mdx'
 lines=p.read_text(encoding='utf-8').splitlines()
 result=[]
 for line in lines:
  if line.startswith('title: '): line=f'title: "{title}"'
  if line.startswith('description: '): line=f'description: "{desc}"'
  if line.startswith('image: '): line=f'image: {image}'
  if line.startswith('summary: '): line=f'summary: "{summary}"'
  result.append(line)
 p.write_text('\n'.join(result)+'\n',encoding='utf-8')
