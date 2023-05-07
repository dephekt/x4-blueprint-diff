# x4-blueprint-diff

For the game X4: Foundations, it lets you compare blueprints that are part
of one custom gamestart XML file with another custom gamestart. This is useful
if you have exported a custom start that X4 will no longer allow you to import
because it claims some blueprints are prohibited.

You can run this script and compare a non-working gamestart with one that works,
and then see the blueprints that aren't in the working one, so you know which
ones to remove.

## Setup

If you have `poetry` installed, you can just clone this repo and install with
`poetry` like:

```
$ git clone https://github.com/dephekt/x4-blueprint-diff
$ cd x4-blueprint-diff
$ poetry install
```

Then run the script like:
```
$ poetry run ./run.py ~/path/to/bad.xml ~/path/to/good.xml
{<ware ware="module_ter_stor_container_m_tradestation"/>,
 <ware ware="module_ter_stor_liquid_s_tradestation"/>,
 <ware ware="module_ter_prod_scrap_recycler"/>,
 <ware ware="paintmod_0006"/>,
 <ware ware="paintmod_0048"/>,
 <ware ware="paintmod_0049"/>,
 <ware ware="paintmod_0050"/>,
 <ware ware="paintmod_0097"/>,
 <ware ware="paintmod_0098"/>,
 <ware ware="paintmod_0099"/>,
 <ware ware="paintmod_0100"/>,
 <ware ware="engine_spacesuit_weak"/>,
 <ware ware="weapon_gen_spacesuit_laser_01_mk1"/>,
 <ware ware="weapon_gen_spacesuit_laser_02_mk1"/>,
 <ware ware="weapon_gen_spacesuit_repairlaser_01_mk1"/>,
 <ware ware="module_gen_prod_scrap_recycler"/>,
 <ware ware="engine_gen_spacesuit_01_mk1"/>,
 <ware ware="engine_gen_spacesuit_01_mk2"/>}
```

If I then remove those blueprints from the bad.xml file and restart X4, the
file should be importable now.

If you don't have `poetry`, you can just use `pip` with a virtual environment:

```
$ python3 -m venv .env
$ .env/bin/pip install -r requirements.txt
$ source .env/bin/activate
$ ./run.py ~/path/to/bad.xml ~/path/to/good.xml
```

## Compatibility

I tested this in Linux using Python 3.10, but it should work for any Python 3
version. It might work in Windows if you have a proper Python development
environment setup and configured, but no guarantees as I've done zero testing
in Windows.
