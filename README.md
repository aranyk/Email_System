# Email_System


<img src="usecase.png" width="200">




<img src="Seq_Diagram.png" width="200">

Sekvensdiagrammet viser systemets hoved- og alternative flyt. Objekt og actors vises på toppen av diagrammet. 
Fra disse ser vi piler som linker til hver objekt.
Her har vi tatt fokus på sortering av epost, uavhengig hvordan det er ønsket å sortere. 

##### _Scenario fra diagram:_
Mail kommer fra mail_register og sendes videre til system. 
Systemet vil fungere som et mellomledd der mail vises fram. 
Dersom det ikke er mulig å sortere som ansatte har valgt, vil bruker få feilmelding og 
muligheten til å sortere andre måter. 

Dersom det er mulig å sortere på ønsket måte, vil mail sorteres og vises fram hos ansatte. 

