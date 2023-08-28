# Antenna for 40m, 20m, 15m, 10m
<a href="./doc/antenna_packed.jpg"><img src="./doc/antenna_packed.jpg" width="500"/></a>

First version of the antenna.  Made on perfboard and using household wire.

## Antenna setup
An SDRplay RSP1A is connected to 10m coax on the ground, which is connected to the EFHW transformer, about 2m above ground.  The left side of the perfboard is connected with a few meters of isulated wire to a fence.  The right side of the perfboard connects to the antenna wire.  The antenna wire is connected to the secondary of the transformer.  The primary and secondary coils of the transformer have a common ground.

The antenna wire is about 20m long, and it loops through a wire which hangs from a window at about 6m above ground.  Then leading back to a fence where it's fixed with an 8S carabiner.

The antenna setup resembles more or less an inverted V.  The angle between the antenna wire and the ground is about 30 degrees.

## VSWR measurement

<a href="./doc/vswr_no_primary_cap.png"><img src="./doc/vswr_no_primary_cap.png" width="500"/></a>

VSWR on 10m is not great.  This might be improved by adding a 100pF capacitor in parallel with the primary coil.  To be tested.

Another option is to add inductance on the antenna wire, near the transformer.  This has been tested by [Gary Rondeau](https://squashpractice.com/2021/07/20/engineering-the-efhw-491-transformer-and-antenna/).


# Parts list
| Item | Description | Qty | Price |
| ---- | ----------- | --- | ----- |
| [Hammond 1551HFLBK](https://www.trustedparts.com/en/part/hammond/1551HFLBK) | Enclosures, Boxes, & Cases Miniature/FlangedLid 2.36x1.38x.79" Black| 1 | €2.71 |
| [Deltron 552-0100 BLK](https://www.trustedparts.com/en/part/deltron-enclosures/552-0100%20BLK) | Test Plugs & Test Jacks INSULATED BLACK  | 1 | €1.38 |
| [AliExpress](https://www.aliexpress.com/item/32991699241.html) | 8s shape carabiner keychain orange | 4| €3.57/10pcs|
| [AliExpress](https://www.aliexpress.com/item/1005002686878536.html) | BNC-M/BNC-M cable, RG316, 5m | 2 | €19.40/2pcs |
| [AliExpress](https://www.aliexpress.com/item/32998333031.html) | F-BNC/F-BNC adapter | 1 | €1.66/2pcs |
| [AliExpress](https://www.aliexpress.com/item/1005001867862900.html) | M-BNC/F-SMA adapter | 1 | €5.64/2pcs |
| [AliExpress](https://www.aliexpress.com/item/33061511845.html) | Red, 50 Meters, 24AWG, UL1571 PVC insulated wire | ±20m | €18.25/50m |

# Notes
* Hammond enclosure idea from [MM0OPX EFHW](https://youtu.be/nZ-G4hJCTSM?t=1123)
* 10m coax cable is integral part of the antenna