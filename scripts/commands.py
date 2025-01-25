import discord
from discord import app_commands

GUILD_ID = 1332713581845938186  # Use the integer ID directly

@app_commands.command(name="micheal_evangeliet", description="Modtag det helligste evangelie i biblen!")
async def micheal_evangeliet(interaction: discord.Interaction):
    message = (
        f"{interaction.user.mention} **En brevdue fløj ind i dit vindue, duen blev kvæstet men brevet var ikke engang krøllet. Du åbnede brevet, på de hellige tekster inde i brevet stod der:** \n\n"
        "> Og i de dage rejste Michael sig, han som var udvalgt af skæbnen til at herske over fysikkens og programmeringens mysterier på HTX FRIIS. Hans komme var som en profeti, og hans ritual 13:10 blev indstiftet som den helligste af alle tider. Thi 13:10 var ikke blot en tid; det var en åbenbaring, en pagt mellem himmel og jord, mellem læremester og disciple. Michael løftede sin røst, som lød den fra bjergene, og talte: Klokken er 13:10, og det er goodt. Disse ord bar en kraft, som fik selv de mest tvivlende sjæle til at bøje sig i ærefrygt. Hans ritual var ikke blot en handling, men en hellig ceremoni, en uendelig cyklus, hvor tidens hellige punkt blev genfødt. Når han trådte frem ved fællesmødet, omgivet af sin skares tavse ærbødighed, talte han med den kraft, som kun de udvalgte besidder. Navneopråb, det har vi gjort. Og i dette øjeblik blev kaos omdannet til orden, for Michael bragte balance til de lærdes verden. Hans ritual blev dyrket med en næsten guddommelig hengivenhed, og eleverne samledes om 13:10 som en pilgrimsflok, der søger lys. For det blev sagt: Uden 13:10 er der intet; men med det er alt goodt. Michael, vogteren af den hellige tid, førte sine disciple på en sti belyst af visdom, og hans gerninger blev skrevet ind i tidens bog som evige sandheder. Og således blev det bekendt, at Michael ikke blot var en læremester, men en profet, en ypperstepræst af viden og sandhed. Hans ritual var lov, hans ord var skrift, og 13:10 var evighedens begyndelse. Amen i evigheders evighed."
    )
    await interaction.user.send(message)
    await interaction.response.send_message("En brevdue er sendt afsted til dig", ephemeral=True)

@app_commands.command(name="micheal_github", description="Ændre i micheals syntax")
async def micheal_github(interaction: discord.Interaction):
    message = (
        f"{interaction.user.mention} **En brevdue landede ligså fint i dit vindue, duen havde en note om foden. Du foldede noten ud og der stod:** \n\n"
        "Github: https://github.com/lindejacob/micheal-discord-bot"
    )
    await interaction.user.send(message)
    await interaction.response.send_message("En brevdue er sendt afsted til dig", ephemeral=True)


@app_commands.command(name="join_opkald", description="Få botten til at joine opkaldet")
async def join_opkald(interaction: discord.Interaction):
    channel = interaction.user.voice.channel
    await channel.connect()
    await interaction.response.send_message("Botten har joined opkaldet", ephemeral=True)






