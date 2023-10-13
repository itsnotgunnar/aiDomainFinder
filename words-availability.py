import csv
import json
from sympy import true, false

domains = [
  {
    "domain": "Ablaze.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Ablaze.ai"
  },
  {
    "domain": "Absolute.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Absolute.ai"
  },
  {
    "domain": "Abundant.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Abundant.ai"
  },
  {
    "domain": "Acclaim.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Acclaim.ai"
  },
  {
    "domain": "Accolade.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Accolade.ai"
  },
  {
    "domain": "Adept.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Adept.ai"
  },
  {
    "domain": "Admire.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Admire.ai"
  },
  {
    "domain": "Adorn.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Adorn.ai"
  },
  {
    "domain": "Advance.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Advance.ai"
  },
  {
    "domain": "Aegis.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Aegis.ai"
  },
  {
    "domain": "Affluent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Affluent.ai"
  },
  {
    "domain": "Agile.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Agile.ai"
  },
  {
    "domain": "Allure.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Allure.ai"
  },
  {
    "domain": "Alpha.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Alpha.ai"
  },
  {
    "domain": "Amaze.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Amaze.ai"
  },
  {
    "domain": "Ambition.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Ambition.ai"
  },
  {
    "domain": "Amplify.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Amplify.ai"
  },
  {
    "domain": "Angelic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Angelic.ai"
  },
  {
    "domain": "Apex.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Apex.ai"
  },
  {
    "domain": "Apogee.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Apogee.ai"
  },
  {
    "domain": "Arcane.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Arcane.ai"
  },
  {
    "domain": "Aria.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Aria.ai"
  },
  {
    "domain": "Ascend.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Ascend.ai"
  },
  {
    "domain": "Aspire.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Aspire.ai"
  },
  {
    "domain": "Astonish.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Astonish.ai"
  },
  {
    "domain": "Atlas.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Atlas.ai"
  },
  {
    "domain": "Aura.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Aura.ai"
  },
  {
    "domain": "Aurora.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Aurora.ai"
  },
  {
    "domain": "Avant-garde.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Avant-garde.ai"
  },
  {
    "domain": "Awe.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Awe.ai"
  },
  {
    "domain": "Balance.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Balance.ai"
  },
  {
    "domain": "Beacon.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Beacon.ai"
  },
  {
    "domain": "Beam.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Beam.ai"
  },
  {
    "domain": "Benevolent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Benevolent.ai"
  },
  {
    "domain": "Blaze.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Blaze.ai"
  },
  {
    "domain": "Bliss.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Bliss.ai"
  },
  {
    "domain": "Bloom.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Bloom.ai"
  },
  {
    "domain": "Blossom.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Blossom.ai"
  },
  {
    "domain": "Bold.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Bold.ai"
  },
  {
    "domain": "Boundless.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Boundless.ai"
  },
  {
    "domain": "Breeze.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Breeze.ai"
  },
  {
    "domain": "Brilliance.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Brilliance.ai"
  },
  {
    "domain": "Brisk.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Brisk.ai"
  },
  {
    "domain": "Brio.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Brio.ai"
  },
  {
    "domain": "Burst.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Burst.ai"
  },
  {
    "domain": "Cadence.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Cadence.ai"
  },
  {
    "domain": "Caliber.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Caliber.ai"
  },
  {
    "domain": "Canvas.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Canvas.ai"
  },
  {
    "domain": "Capstone.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Capstone.ai"
  },
  {
    "domain": "Cascade.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Cascade.ai"
  },
  {
    "domain": "Celestial.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Celestial.ai"
  },
  {
    "domain": "Champion.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Champion.ai"
  },
  {
    "domain": "Charisma.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Charisma.ai"
  },
  {
    "domain": "Charm.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Charm.ai"
  },
  {
    "domain": "Chateau.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Chateau.ai"
  },
  {
    "domain": "Cherish.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Cherish.ai"
  },
  {
    "domain": "Clarity.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Clarity.ai"
  },
  {
    "domain": "Classic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Classic.ai"
  },
  {
    "domain": "Clever.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Clever.ai"
  },
  {
    "domain": "Climb.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Climb.ai"
  },
  {
    "domain": "Cloud.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Cloud.ai"
  },
  {
    "domain": "Coast.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Coast.ai"
  },
  {
    "domain": "Cohesive.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Cohesive.ai"
  },
  {
    "domain": "Colossal.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Colossal.ai"
  },
  {
    "domain": "Comet.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Comet.ai"
  },
  {
    "domain": "Command.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Command.ai"
  },
  {
    "domain": "Compass.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Compass.ai"
  },
  {
    "domain": "Conquer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Conquer.ai"
  },
  {
    "domain": "Constellation.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Constellation.ai"
  },
  {
    "domain": "Contour.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Contour.ai"
  },
  {
    "domain": "Core.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Core.ai"
  },
  {
    "domain": "Coronet.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/Coronet.ai"
  },
  {
    "domain": "Cosmic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Cosmic.ai"
  },
  {
    "domain": "Crave.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Crave.ai"
  },
  {
    "domain": "Crest.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Crest.ai"
  },
  {
    "domain": "Crown.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Crown.ai"
  },
  {
    "domain": "Crystal.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Crystal.ai"
  },
  {
    "domain": "Cultivate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Cultivate.ai"
  },
  {
    "domain": "Curate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Curate.ai"
  },
  {
    "domain": "Dazzle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Dazzle.ai"
  },
  {
    "domain": "Decipher.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Decipher.ai"
  },
  {
    "domain": "Delight.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Delight.ai"
  },
  {
    "domain": "Deluxe.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Deluxe.ai"
  },
  {
    "domain": "Destiny.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Destiny.ai"
  },
  {
    "domain": "Diamond.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Diamond.ai"
  },
  {
    "domain": "Divine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Divine.ai"
  },
  {
    "domain": "Dream.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Dream.ai"
  },
  {
    "domain": "Drift.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Drift.ai"
  },
  {
    "domain": "Dynamic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Dynamic.ai"
  },
  {
    "domain": "Echo.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Echo.ai"
  },
  {
    "domain": "Eclipse.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Eclipse.ai"
  },
  {
    "domain": "Eden.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Eden.ai"
  },
  {
    "domain": "Edge.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Edge.ai"
  },
  {
    "domain": "Efficacy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Efficacy.ai"
  },
  {
    "domain": "Elation.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Elation.ai"
  },
  {
    "domain": "Elite.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Elite.ai"
  },
  {
    "domain": "Ember.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Ember.ai"
  },
  {
    "domain": "Emblaze.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Emblaze.ai"
  },
  {
    "domain": "Embrace.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Embrace.ai"
  },
  {
    "domain": "Emerge.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Emerge.ai"
  },
  {
    "domain": "Empower.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Empower.ai"
  },
  {
    "domain": "Enchant.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Enchant.ai"
  },
  {
    "domain": "Endless.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Endless.ai"
  },
  {
    "domain": "Enhance.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Enhance.ai"
  },
  {
    "domain": "Enigma.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Enigma.ai"
  },
  {
    "domain": "Enliven.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Enliven.ai"
  },
  {
    "domain": "Eon.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Eon.ai"
  },
  {
    "domain": "Epic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Epic.ai"
  },
  {
    "domain": "Epoch.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Epoch.ai"
  },
  {
    "domain": "Equinox.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Equinox.ai"
  },
  {
    "domain": "Essence.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Essence.ai"
  },
  {
    "domain": "Ethereal.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Ethereal.ai"
  },
  {
    "domain": "Euphoria.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Euphoria.ai"
  },
  {
    "domain": "Evolve.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Evolve.ai"
  },
  {
    "domain": "Exalt.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Exalt.ai"
  },
  {
    "domain": "Excel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Excel.ai"
  },
  {
    "domain": "Exquisite.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Exquisite.ai"
  },
  {
    "domain": "Extravagant.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/Extravagant.ai"
  },
  {
    "domain": "Exuberant.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Exuberant.ai"
  },
  {
    "domain": "Facet.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Facet.ai"
  },
  {
    "domain": "Fathom.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Fathom.ai"
  },
  {
    "domain": "Felicity.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Felicity.ai"
  },
  {
    "domain": "Finesse.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Finesse.ai"
  },
  {
    "domain": "Flair.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Flair.ai"
  },
  {
    "domain": "Flourish.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Flourish.ai"
  },
  {
    "domain": "Flow.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Flow.ai"
  },
  {
    "domain": "Flourish.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Flourish.ai"
  },
  {
    "domain": "Focus.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Focus.ai"
  },
  {
    "domain": "Forte.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Forte.ai"
  },
  {
    "domain": "Fortune.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Fortune.ai"
  },
  {
    "domain": "Free.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Free.ai"
  },
  {
    "domain": "Fresh.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Fresh.ai"
  },
  {
    "domain": "Fusion.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Fusion.ai"
  },
  {
    "domain": "Gale.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Gale.ai"
  },
  {
    "domain": "Galaxy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Galaxy.ai"
  },
  {
    "domain": "Gem.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Gem.ai"
  },
  {
    "domain": "Genesis.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Genesis.ai"
  },
  {
    "domain": "Glimmer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Glimmer.ai"
  },
  {
    "domain": "Glint.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Glint.ai"
  },
  {
    "domain": "Glitz.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Glitz.ai"
  },
  {
    "domain": "Glow.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Glow.ai"
  },
  {
    "domain": "Grace.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Grace.ai"
  },
  {
    "domain": "Grandeur.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Grandeur.ai"
  },
  {
    "domain": "Gravitas.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Gravitas.ai"
  },
  {
    "domain": "Halo.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Halo.ai"
  },
  {
    "domain": "Harmony.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Harmony.ai"
  },
  {
    "domain": "Haven.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Haven.ai"
  },
  {
    "domain": "Helix.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Helix.ai"
  },
  {
    "domain": "Horizon.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Horizon.ai"
  },
  {
    "domain": "Hub.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Hub.ai"
  },
  {
    "domain": "Hue.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Hue.ai"
  },
  {
    "domain": "Illuminate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Illuminate.ai"
  },
  {
    "domain": "Illustrious.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Illustrious.ai"
  },
  {
    "domain": "Imagine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Imagine.ai"
  },
  {
    "domain": "Immerse.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Immerse.ai"
  },
  {
    "domain": "Impact.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Impact.ai"
  },
  {
    "domain": "Imperial.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Imperial.ai"
  },
  {
    "domain": "Incandescent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Incandescent.ai"
  },
  {
    "domain": "Inception.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Inception.ai"
  },
  {
    "domain": "Infinite.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Infinite.ai"
  },
  {
    "domain": "Influx.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Influx.ai"
  },
  {
    "domain": "Inspire.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Inspire.ai"
  },
  {
    "domain": "Instinct.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Instinct.ai"
  },
  {
    "domain": "Integrate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Integrate.ai"
  },
  {
    "domain": "Intense.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Intense.ai"
  },
  {
    "domain": "Interstellar.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Interstellar.ai"
  },
  {
    "domain": "Intrigue.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Intrigue.ai"
  },
  {
    "domain": "Invigorate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Invigorate.ai"
  },
  {
    "domain": "Iridescent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Iridescent.ai"
  },
  {
    "domain": "Jewel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Jewel.ai"
  },
  {
    "domain": "Journey.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Journey.ai"
  },
  {
    "domain": "Jubilant.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Jubilant.ai"
  },
  {
    "domain": "Kaleidoscope.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Kaleidoscope.ai"
  },
  {
    "domain": "Keystone.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Keystone.ai"
  },
  {
    "domain": "Kinetic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Kinetic.ai"
  },
  {
    "domain": "Kingdom.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Kingdom.ai"
  },
  {
    "domain": "Labyrinth.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Labyrinth.ai"
  },
  {
    "domain": "Latch.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Latch.ai"
  },
  {
    "domain": "Legacy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Legacy.ai"
  },
  {
    "domain": "Legend.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Legend.ai"
  },
  {
    "domain": "Lighthouse.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Lighthouse.ai"
  },
  {
    "domain": "Liminal.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Liminal.ai"
  },
  {
    "domain": "Luminous.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Luminous.ai"
  },
  {
    "domain": "Luxe.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Luxe.ai"
  },
  {
    "domain": "Lyric.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Lyric.ai"
  },
  {
    "domain": "Magic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Magic.ai"
  },
  {
    "domain": "Magna.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Magna.ai"
  },
  {
    "domain": "Magnify.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Magnify.ai"
  },
  {
    "domain": "Majesty.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Majesty.ai"
  },
  {
    "domain": "Marvel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Marvel.ai"
  },
  {
    "domain": "Masquerade.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Masquerade.ai"
  },
  {
    "domain": "Matrix.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Matrix.ai"
  },
  {
    "domain": "Maven.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Maven.ai"
  },
  {
    "domain": "Maximize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Maximize.ai"
  },
  {
    "domain": "Melody.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Melody.ai"
  },
  {
    "domain": "Meridian.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Meridian.ai"
  },
  {
    "domain": "Mesmerize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Mesmerize.ai"
  },
  {
    "domain": "Metamorphosis.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Metamorphosis.ai"
  },
  {
    "domain": "Meteor.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Meteor.ai"
  },
  {
    "domain": "Mingle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Mingle.ai"
  },
  {
    "domain": "Mirage.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Mirage.ai"
  },
  {
    "domain": "Mirth.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Mirth.ai"
  },
  {
    "domain": "Mist.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Mist.ai"
  },
  {
    "domain": "Mosaic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Mosaic.ai"
  },
  {
    "domain": "Motion.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Motion.ai"
  },
  {
    "domain": "Muse.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Muse.ai"
  },
  {
    "domain": "Mystic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Mystic.ai"
  },
  {
    "domain": "Nebula.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Nebula.ai"
  },
  {
    "domain": "Nexus.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Nexus.ai"
  },
  {
    "domain": "Nirvana.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Nirvana.ai"
  },
  {
    "domain": "Noble.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Noble.ai"
  },
  {
    "domain": "Nova.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Nova.ai"
  },
  {
    "domain": "Oasis.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Oasis.ai"
  },
  {
    "domain": "Odyssey.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Odyssey.ai"
  },
  {
    "domain": "Opulent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Opulent.ai"
  },
  {
    "domain": "Oracle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Oracle.ai"
  },
  {
    "domain": "Orbit.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Orbit.ai"
  },
  {
    "domain": "Ovation.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Ovation.ai"
  },
  {
    "domain": "Overlook.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Overlook.ai"
  },
  {
    "domain": "Panache.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Panache.ai"
  },
  {
    "domain": "Panorama.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Panorama.ai"
  },
  {
    "domain": "Paragon.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Paragon.ai"
  },
  {
    "domain": "Passion.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Passion.ai"
  },
  {
    "domain": "Peak.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Peak.ai"
  },
  {
    "domain": "Pinnacle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Pinnacle.ai"
  },
  {
    "domain": "Pixel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Pixel.ai"
  },
  {
    "domain": "Plume.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Plume.ai"
  },
  {
    "domain": "Poise.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Poise.ai"
  },
  {
    "domain": "Polished.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Polished.ai"
  },
  {
    "domain": "Portal.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Portal.ai"
  },
  {
    "domain": "Posh.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Posh.ai"
  },
  {
    "domain": "Prestige.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Prestige.ai"
  },
  {
    "domain": "Prime.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Prime.ai"
  },
  {
    "domain": "Prism.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Prism.ai"
  },
  {
    "domain": "Prodigy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Prodigy.ai"
  },
  {
    "domain": "Prosper.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Prosper.ai"
  },
  {
    "domain": "Pulse.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Pulse.ai"
  },
  {
    "domain": "Purity.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Purity.ai"
  },
  {
    "domain": "Quest.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Quest.ai"
  },
  {
    "domain": "Quill.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Quill.ai"
  },
  {
    "domain": "Quintessence.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Quintessence.ai"
  },
  {
    "domain": "Radiance.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Radiance.ai"
  },
  {
    "domain": "Rapture.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rapture.ai"
  },
  {
    "domain": "Rare.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rare.ai"
  },
  {
    "domain": "Rave.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rave.ai"
  },
  {
    "domain": "Realm.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Realm.ai"
  },
  {
    "domain": "Rebirth.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rebirth.ai"
  },
  {
    "domain": "Refined.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Refined.ai"
  },
  {
    "domain": "Regal.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Regal.ai"
  },
  {
    "domain": "Reign.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Reign.ai"
  },
  {
    "domain": "Rejuvenate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rejuvenate.ai"
  },
  {
    "domain": "Relish.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Relish.ai"
  },
  {
    "domain": "Renaissance.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Renaissance.ai"
  },
  {
    "domain": "Resonate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Resonate.ai"
  },
  {
    "domain": "Rhapsody.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rhapsody.ai"
  },
  {
    "domain": "Rhythm.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rhythm.ai"
  },
  {
    "domain": "Rich.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rich.ai"
  },
  {
    "domain": "Rise.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rise.ai"
  },
  {
    "domain": "Riviera.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Riviera.ai"
  },
  {
    "domain": "Roam.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Roam.ai"
  },
  {
    "domain": "Royal.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Royal.ai"
  },
  {
    "domain": "Ruby.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Ruby.ai"
  },
  {
    "domain": "Rumble.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rumble.ai"
  },
  {
    "domain": "Sanctuary.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Sanctuary.ai"
  },
  {
    "domain": "Sapphire.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Sapphire.ai"
  },
  {
    "domain": "Satin.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Satin.ai"
  },
  {
    "domain": "Savvy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Savvy.ai"
  },
  {
    "domain": "Scepter.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Scepter.ai"
  },
  {
    "domain": "Serene.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Serene.ai"
  },
  {
    "domain": "Shimmer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Shimmer.ai"
  },
  {
    "domain": "Shine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Shine.ai"
  },
  {
    "domain": "Silhouette.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Silhouette.ai"
  },
  {
    "domain": "Silk.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Silk.ai"
  },
  {
    "domain": "Silver.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Silver.ai"
  },
  {
    "domain": "Skyline.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Skyline.ai"
  },
  {
    "domain": "Sleek.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Sleek.ai"
  },
  {
    "domain": "Solstice.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Solstice.ai"
  },
  {
    "domain": "Sonata.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Sonata.ai"
  },
  {
    "domain": "Sophisticate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Sophisticate.ai"
  },
  {
    "domain": "Spark.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Spark.ai"
  },
  {
    "domain": "Spectrum.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Spectrum.ai"
  },
  {
    "domain": "Spellbind.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Spellbind.ai"
  },
  {
    "domain": "Spirit.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Spirit.ai"
  },
  {
    "domain": "Splendor.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Splendor.ai"
  },
  {
    "domain": "Spontaneous.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Spontaneous.ai"
  },
  {
    "domain": "Spring.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Spring.ai"
  },
  {
    "domain": "Star.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Star.ai"
  },
  {
    "domain": "Stellar.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Stellar.ai"
  },
  {
    "domain": "Strive.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Strive.ai"
  },
  {
    "domain": "Summit.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Summit.ai"
  },
  {
    "domain": "Sunburst.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Sunburst.ai"
  },
  {
    "domain": "Sunrise.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Sunrise.ai"
  },
  {
    "domain": "Supreme.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Supreme.ai"
  },
  {
    "domain": "Surge.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Surge.ai"
  },
  {
    "domain": "Sway.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Sway.ai"
  },
  {
    "domain": "Symphony.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Symphony.ai"
  },
  {
    "domain": "Synthesis.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Synthesis.ai"
  },
  {
    "domain": "Tapestry.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Tapestry.ai"
  },
  {
    "domain": "Tease.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Tease.ai"
  },
  {
    "domain": "Tempo.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Tempo.ai"
  },
  {
    "domain": "Tenor.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Tenor.ai"
  },
  {
    "domain": "Terra.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Terra.ai"
  },
  {
    "domain": "Thrive.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Thrive.ai"
  },
  {
    "domain": "Tidal.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Tidal.ai"
  },
  {
    "domain": "Timeless.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Timeless.ai"
  },
  {
    "domain": "Titan.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Titan.ai"
  },
  {
    "domain": "Topaz.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Topaz.ai"
  },
  {
    "domain": "Trace.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Trace.ai"
  },
  {
    "domain": "Tranquil.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Tranquil.ai"
  },
  {
    "domain": "Treasure.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Treasure.ai"
  },
  {
    "domain": "Triumph.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Triumph.ai"
  },
  {
    "domain": "Twilight.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Twilight.ai"
  },
  {
    "domain": "Twin.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Twin.ai"
  },
  {
    "domain": "Ultimate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Ultimate.ai"
  },
  {
    "domain": "Ultra.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Ultra.ai"
  },
  {
    "domain": "Unison.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Unison.ai"
  },
  {
    "domain": "Universe.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Universe.ai"
  },
  {
    "domain": "Uplift.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Uplift.ai"
  },
  {
    "domain": "Utopia.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Utopia.ai"
  },
  {
    "domain": "Valor.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Valor.ai"
  },
  {
    "domain": "Vanguard.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Vanguard.ai"
  },
  {
    "domain": "Velvet.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Velvet.ai"
  },
  {
    "domain": "vivacious.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/vivacious.ai"
  },
  {
    "domain": "effervescent.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/effervescent.ai"
  },
  {
    "domain": "energetic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/energetic.ai"
  },
  {
    "domain": "vigorous.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/vigorous.ai"
  },
  {
    "domain": "dynamic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/dynamic.ai"
  },
  {
    "domain": "spirited.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/spirited.ai"
  },
  {
    "domain": "lively.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/lively.ai"
  },
  {
    "domain": "animated.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/animated.ai"
  },
  {
    "domain": "sparkling.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sparkling.ai"
  },
  {
    "domain": "bouncy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bouncy.ai"
  },
  {
    "domain": "bubbly.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bubbly.ai"
  },
  {
    "domain": "peppy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/peppy.ai"
  },
  {
    "domain": "sprightly.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sprightly.ai"
  },
  {
    "domain": "spunky.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/spunky.ai"
  },
  {
    "domain": "playful.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/playful.ai"
  },
  {
    "domain": "frisky.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/frisky.ai"
  },
  {
    "domain": "perky.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/perky.ai"
  },
  {
    "domain": "chirpy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/chirpy.ai"
  },
  {
    "domain": "cheerful.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cheerful.ai"
  },
  {
    "domain": "bright.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bright.ai"
  },
  {
    "domain": "sunny.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sunny.ai"
  },
  {
    "domain": "dazzling.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/dazzling.ai"
  },
  {
    "domain": "radiant.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/radiant.ai"
  },
  {
    "domain": "glowing.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/glowing.ai"
  },
  {
    "domain": "shimmering.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/shimmering.ai"
  },
  {
    "domain": "twinkling.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/twinkling.ai"
  },
  {
    "domain": "scintillat.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/scintillat.ai"
  },
  {
    "domain": "excited.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/excited.ai"
  },
  {
    "domain": "thrilled.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/thrilled.ai"
  },
  {
    "domain": "exhilarated.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/exhilarated.ai"
  },
  {
    "domain": "invigorated.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/invigorated.ai"
  },
  {
    "domain": "rejuvenated.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/rejuvenated.ai"
  },
  {
    "domain": "restorative.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/restorative.ai"
  },
  {
    "domain": "revitalized.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/revitalized.ai"
  },
  {
    "domain": "stimulated.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/stimulated.ai"
  },
  {
    "domain": "electrify.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/electrify.ai"
  },
  {
    "domain": "tantalized.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/tantalized.ai"
  },
  {
    "domain": "vibrant.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/vibrant.ai"
  },
  {
    "domain": "pulse.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/pulse.ai"
  },
  {
    "domain": "throb.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/throb.ai"
  },
  {
    "domain": "alive.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/alive.ai"
  },
  {
    "domain": "amaze.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/amaze.ai"
  },
  {
    "domain": "astound.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/astound.ai"
  },
  {
    "domain": "awe-inspir.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/awe-inspir.ai"
  },
  {
    "domain": "awesome.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/awesome.ai"
  },
  {
    "domain": "dazzle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/dazzle.ai"
  },
  {
    "domain": "extraordinary.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/extraordinary.ai"
  },
  {
    "domain": "fascinate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/fascinate.ai"
  },
  {
    "domain": "incred.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/incred.ai"
  },
  {
    "domain": "magical.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/magical.ai"
  },
  {
    "domain": "magnificent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/magnificent.ai"
  },
  {
    "domain": "marvelous.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/marvelous.ai"
  },
  {
    "domain": "miraculous.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/miraculous.ai"
  },
  {
    "domain": "phenomenal.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/phenomenal.ai"
  },
  {
    "domain": "remark.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/remark.ai"
  },
  {
    "domain": "spectacular.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/spectacular.ai"
  },
  {
    "domain": "stagger.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/stagger.ai"
  },
  {
    "domain": "strike.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/strike.ai"
  },
  {
    "domain": "stupendous.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/stupendous.ai"
  },
  {
    "domain": "stun.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/stun.ai"
  },
  {
    "domain": "wondrous.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/wondrous.ai"
  },
  {
    "domain": "abundant.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/abundant.ai"
  },
  {
    "domain": "bountiful.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bountiful.ai"
  },
  {
    "domain": "copious.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/copious.ai"
  },
  {
    "domain": "exuberant.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/exuberant.ai"
  },
  {
    "domain": "lush.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/lush.ai"
  },
  {
    "domain": "plenteiful.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/plenteiful.ai"
  },
  {
    "domain": "profuse.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/profuse.ai"
  },
  {
    "domain": "rich.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/rich.ai"
  },
  {
    "domain": "lavish.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/lavish.ai"
  },
  {
    "domain": "colorful.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/colorful.ai"
  },
  {
    "domain": "vivid.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/vivid.ai"
  },
  {
    "domain": "bright.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bright.ai"
  },
  {
    "domain": "dazzle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/dazzle.ai"
  },
  {
    "domain": "flashy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/flashy.ai"
  },
  {
    "domain": "flamboyant.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/flamboyant.ai"
  },
  {
    "domain": "gaudy.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/gaudy.ai"
  },
  {
    "domain": "glitzy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/glitzy.ai"
  },
  {
    "domain": "ostentatious.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/ostentatious.ai"
  },
  {
    "domain": "showy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/showy.ai"
  },
  {
    "domain": "snazzy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/snazzy.ai"
  },
  {
    "domain": "swanky.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/swanky.ai"
  },
  {
    "domain": "iridescent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/iridescent.ai"
  },
  {
    "domain": "kaleidoscopic.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/kaleidoscopic.ai"
  },
  {
    "domain": "prismatic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/prismatic.ai"
  },
  {
    "domain": "pearly.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/pearly.ai"
  },
  {
    "domain": "shimmery.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/shimmery.ai"
  },
  {
    "domain": "lustrous.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/lustrous.ai"
  },
  {
    "domain": "luminous.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/luminous.ai"
  },
  {
    "domain": "incandescent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/incandescent.ai"
  },
  {
    "domain": "sparkle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sparkle.ai"
  },
  {
    "domain": "glitter.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/glitter.ai"
  },
  {
    "domain": "glimmer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/glimmer.ai"
  },
  {
    "domain": "incandescent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/incandescent.ai"
  },
  {
    "domain": "sparkle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sparkle.ai"
  },
  {
    "domain": "glitter.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/glitter.ai"
  },
  {
    "domain": "glimmer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/glimmer.ai"
  },
  {
    "domain": "scintillate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/scintillate.ai"
  },
  {
    "domain": "crystalline.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/crystalline.ai"
  },
  {
    "domain": "translucent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/translucent.ai"
  },
  {
    "domain": "pellucid.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/pellucid.ai"
  },
  {
    "domain": "limpid.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/limpid.ai"
  },
  {
    "domain": "lucid.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/lucid.ai"
  },
  {
    "domain": "transparent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/transparent.ai"
  },
  {
    "domain": "diaphanous.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/diaphanous.ai"
  },
  {
    "domain": "airy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/airy.ai"
  },
  {
    "domain": "wispy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/wispy.ai"
  },
  {
    "domain": "frothy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/frothy.ai"
  },
  {
    "domain": "foamy.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/foamy.ai"
  },
  {
    "domain": "light.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/light.ai"
  },
  {
    "domain": "feathery.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/feathery.ai"
  },
  {
    "domain": "silky.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/silky.ai"
  },
  {
    "domain": "silvery.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/silvery.ai"
  },
  {
    "domain": "ethereal.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ethereal.ai"
  },
  {
    "domain": "gossamer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/gossamer.ai"
  },
  {
    "domain": "delicate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/delicat.ai"
  },
  {
    "domain": "sheer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sheer.ai"
  },
  {
    "domain": "diaphanous.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/diaphanous.ai"
  },
  {
    "domain": "filmy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/filmy.ai"
  },
  {
    "domain": "gauzy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/gauzy.ai"
  },
  {
    "domain": "vaporous.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/vaporous.ai"
  },
  {
    "domain": "cloudlike.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/cloudlike.ai"
  },
  {
    "domain": "evocativ.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/evocativ.ai"
  },
  {
    "domain": "expressiv.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/expressiv.ai"
  },
  {
    "domain": "illustrativ.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/illustrativ.ai"
  },
  {
    "domain": "meaningful.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/meaningful.ai"
  },
  {
    "domain": "moving.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/moving.ai"
  },
  {
    "domain": "poignante.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/poignante.ai"
  },
  {
    "domain": "provocativ.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/provocativ.ai"
  },
  {
    "domain": "revealing.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/revealing.ai"
  },
  {
    "domain": "suggestiv.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/suggestiv.ai"
  },
  {
    "domain": "touching.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/touching.ai"
  },
  {
    "domain": "rousing.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/rousing.ai"
  },
  {
    "domain": "stir.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/stir.ai"
  },
  {
    "domain": "galvanize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/galvanize.ai"
  },
  {
    "domain": "impel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/impel.ai"
  },
  {
    "domain": "propel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/propel.ai"
  },
  {
    "domain": "spur.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/spur.ai"
  },
  {
    "domain": "stimulate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/stimulate.ai"
  },
  {
    "domain": "stir up.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/stir up.ai"
  },
  {
    "domain": "whip up.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/whip up.ai"
  },
  {
    "domain": "activate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/activate.ai"
  },
  {
    "domain": "animate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/animate.ai"
  },
  {
    "domain": "enliven.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/enliven.ai"
  },
  {
    "domain": "invigorate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/invigorate.ai"
  },
  {
    "domain": "vitaliz.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/vitaliz.ai"
  },
  {
    "domain": "vivify.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/vivify.ai"
  },
  {
    "domain": "awaken.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/awaken.ai"
  },
  {
    "domain": "enliven.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/enliven.ai"
  },
  {
    "domain": "quick.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/quick.ai"
  },
  {
    "domain": "refresh.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/refresh.ai"
  },
  {
    "domain": "rejuvenate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/rejuvenate.ai"
  },
  {
    "domain": "renew.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/renew.ai"
  },
  {
    "domain": "restor.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/restor.ai"
  },
  {
    "domain": "reviv.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/reviv.ai"
  },
  {
    "domain": "exhilarate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/exhilarate.ai"
  },
  {
    "domain": "sparkle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sparkle.ai"
  },
  {
    "domain": "twinkle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/twinkle.ai"
  },
  {
    "domain": "glint.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/glint.ai"
  },
  {
    "domain": "glimmer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/glimmer.ai"
  },
  {
    "domain": "shimmer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/shimmer.ai"
  },
  {
    "domain": "bedazzle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bedazzle.ai"
  },
  {
    "domain": "dazzle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/dazzle.ai"
  },
  {
    "domain": "glisten.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/glisten.ai"
  },
  {
    "domain": "gleam.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/gleam.ai"
  },
  {
    "domain": "shine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/shine.ai"
  },
  {
    "domain": "colorful.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/colorful.ai"
  },
  {
    "domain": "glow.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/glow.ai"
  },
  {
    "domain": "illuminate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/illuminate.ai"
  },
  {
    "domain": "irradiate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/irradiate.ai"
  },
  {
    "domain": "brighten.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/brighten.ai"
  },
  {
    "domain": "shine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/shine.ai"
  },
  {
    "domain": "shimmer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/shimmer.ai"
  },
  {
    "domain": "sparkle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sparkle.ai"
  },
  {
    "domain": "twinkle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/twinkle.ai"
  },
  {
    "domain": "blink.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/blink.ai"
  },
  {
    "domain": "flare.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/flare.ai"
  },
  {
    "domain": "flash.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/flash.ai"
  },
  {
    "domain": "glimmer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/glimmer.ai"
  },
  {
    "domain": "glare.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/glare.ai"
  },
  {
    "domain": "gleam.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/gleam.ai"
  },
  {
    "domain": "glint.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/glint.ai"
  },
  {
    "domain": "glitter.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/glitter.ai"
  },
  {
    "domain": "gloss.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/gloss.ai"
  },
  {
    "domain": "phosphor.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/phosphor.ai"
  },
  {
    "domain": "dance.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/danc.ai"
  },
  {
    "domain": "flicker.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/flicker.ai"
  },
  {
    "domain": "glister.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/glister.ai"
  },
  {
    "domain": "glow.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/glow.ai"
  },
  {
    "domain": "incandesce.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/incandesce.ai"
  },
  {
    "domain": "quiver.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/quiver.ai"
  },
  {
    "domain": "radiate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/radiate.ai"
  },
  {
    "domain": "schiller.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/schiller.ai"
  },
  {
    "domain": "shine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/shine.ai"
  },
  {
    "domain": "shiver.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/shiver.ai"
  },
  {
    "domain": "waver.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/waver.ai"
  },
  {
    "domain": "tremble.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/tremble.ai"
  },
  {
    "domain": "vibrate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/vibrate.ai"
  },
  {
    "domain": "quiver.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/quiver.ai"
  },
  {
    "domain": "shimmer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/shimmer.ai"
  },
  {
    "domain": "undulate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/undulate.ai"
  },
  {
    "domain": "flutter.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/flutter.ai"
  },
  {
    "domain": "ripple.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ripple.ai"
  },
  {
    "domain": "flicker.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/flicker.ai"
  },
  {
    "domain": "waver.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/waver.ai"
  },
  {
    "domain": "oscill.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/oscill.ai"
  },
  {
    "domain": "puls.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/puls.ai"
  },
  {
    "domain": "vibr.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/vibr.ai"
  },
  {
    "domain": "rock.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/rock.ai"
  },
  {
    "domain": "sway.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sway.ai"
  },
  {
    "domain": "swing.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/swing.ai"
  },
  {
    "domain": "ebb.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ebb.ai"
  },
  {
    "domain": "flow.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/flow.ai"
  },
  {
    "domain": "splash.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/splash.ai"
  },
  {
    "domain": "ripple.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ripple.ai"
  },
  {
    "domain": "swirl.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/swirl.ai"
  },
  {
    "domain": "whirl.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/whirl.ai"
  },
  {
    "domain": "churn.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/churn.ai"
  },
  {
    "domain": "bubble.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bubble.ai"
  },
  {
    "domain": "burble.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/burble.ai"
  },
  {
    "domain": "eddy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/eddy.ai"
  },
  {
    "domain": "froth.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/froth.ai"
  },
  {
    "domain": "surge.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/surge.ai"
  },
  {
    "domain": "swash.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/swash.ai"
  },
  {
    "domain": "wash.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/wash.ai"
  },
  {
    "domain": "wave.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/wave.ai"
  },
  {
    "domain": "flutter.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/flutter.ai"
  },
  {
    "domain": "tremble.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/tremble.ai"
  },
  {
    "domain": "quiver.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/quiver.ai"
  },
  {
    "domain": "shiver.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/shiver.ai"
  },
  {
    "domain": "shudder.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/shudder.ai"
  },
  {
    "domain": "shake.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/shake.ai"
  },
  {
    "domain": "quaver.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/quaver.ai"
  },
  {
    "domain": "palpitate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/palpitate.ai"
  },
  {
    "domain": "puls.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/puls.ai"
  },
  {
    "domain": "throb.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/throb.ai"
  },
  {
    "domain": "pound.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/pound.ai"
  },
  {
    "domain": "thrum.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/thrum.ai"
  },
  {
    "domain": "thump.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/thump.ai"
  },
  {
    "domain": "rumble.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/rumble.ai"
  },
  {
    "domain": "resound.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/resound.ai"
  },
  {
    "domain": "reverberate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/reverberate.ai"
  },
  {
    "domain": "echo.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/echo.ai"
  },
  {
    "domain": "resonate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/resonate.ai"
  },
  {
    "domain": "ring.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ring.ai"
  },
  {
    "domain": "toll.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/toll.ai"
  },
  {
    "domain": "peal.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/peal.ai"
  },
  {
    "domain": "chime.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/chime.ai"
  },
  {
    "domain": "clang.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/clang.ai"
  },
  {
    "domain": "crash.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/crash.ai"
  },
  {
    "domain": "clap.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/clap.ai"
  },
  {
    "domain": "crack.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/crack.ai"
  },
  {
    "domain": "pop.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/pop.ai"
  },
  {
    "domain": "snap.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/snap.ai"
  },
  {
    "domain": "whack.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/whack.ai"
  },
  {
    "domain": "smack.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/smack.ai"
  },
  {
    "domain": "wham.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/wham.ai"
  },
  {
    "domain": "bam.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bam.ai"
  },
  {
    "domain": "bang.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bang.ai"
  },
  {
    "domain": "boom.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/boom.ai"
  },
  {
    "domain": "roar.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/roar.ai"
  },
  {
    "domain": "thunder.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/thunder.ai"
  },
  {
    "domain": "blast.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/blast.ai"
  },
  {
    "domain": "resound.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/resound.ai"
  },
  {
    "domain": "rumble.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/rumble.ai"
  },
  {
    "domain": "boom.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/boom.ai"
  },
  {
    "domain": "explode.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/explode.ai"
  },
  {
    "domain": "detonate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/detonate.ai"
  },
  {
    "domain": "Wanderlust.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Wanderlust.ai"
  },
  {
    "domain": "Daydream.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Daydream.ai"
  },
  {
    "domain": "Pixie.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Pixie.ai"
  },
  {
    "domain": "Firefly.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Firefly.ai"
  },
  {
    "domain": "Lemon.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Lemon.ai"
  },
  {
    "domain": "Sunbeam.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Sunbeam.ai"
  },
  {
    "domain": "Buttercup.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Buttercup.ai"
  },
  {
    "domain": "Blue.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Blue.ai"
  },
  {
    "domain": "Free.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Free.ai"
  },
  {
    "domain": "Bright.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Bright.ai"
  },
  {
    "domain": "Lucky.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Lucky.ai"
  },
  {
    "domain": "Wildflower.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Wildflower.ai"
  },
  {
    "domain": "Summer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Summer.ai"
  },
  {
    "domain": "Horizon.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Horizon.ai"
  },
  {
    "domain": "Hummingbird.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Hummingbird.ai"
  },
  {
    "domain": "Firefly.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Firefly.ai"
  },
  {
    "domain": "Rising.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rising.ai"
  },
  {
    "domain": "Bold.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Bold.ai"
  },
  {
    "domain": "Visionary.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Visionary.ai"
  },
  {
    "domain": "Trailblazer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Trailblazer.ai"
  },
  {
    "domain": "Maverick.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Maverick.ai"
  },
  {
    "domain": "Voyager.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Voyager.ai"
  },
  {
    "domain": "Pioneer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Pioneer.ai"
  },
  {
    "domain": "Think.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Think.ai"
  },
  {
    "domain": "Genius.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Genius.ai"
  },
  {
    "domain": "Idea.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Idea.ai"
  },
  {
    "domain": "Brainstorm.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Brainstorm.ai"
  },
  {
    "domain": "Clever.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Clever.ai"
  },
  {
    "domain": "Wise.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Wise.ai"
  },
  {
    "domain": "Inspire.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Inspire.ai"
  },
  {
    "domain": "Enlighten.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Enlighten.ai"
  },
  {
    "domain": "Empower.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Empower.ai"
  },
  {
    "domain": "Bloom.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Bloom.ai"
  },
  {
    "domain": "Blossom.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Blossom.ai"
  },
  {
    "domain": "Grow.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Grow.ai"
  },
  {
    "domain": "Sprout.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Sprout.ai"
  },
  {
    "domain": "Seedling.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Seedling.ai"
  },
  {
    "domain": "Bud.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Bud.ai"
  },
  {
    "domain": "Sapling.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Sapling.ai"
  },
  {
    "domain": "Leaf.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Leaf.ai"
  },
  {
    "domain": "Branch.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Branch.ai"
  },
  {
    "domain": "Root.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Root.ai"
  },
  {
    "domain": "Spark.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Spark.ai"
  },
  {
    "domain": "Ignite.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Ignite.ai"
  },
  {
    "domain": "Luminary.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Luminary.ai"
  },
  {
    "domain": "Beacon.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Beacon.ai"
  },
  {
    "domain": "Torch.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Torch.ai"
  },
  {
    "domain": "Prism.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Prism.ai"
  },
  {
    "domain": "Kaleidoscope.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Kaleidoscope.ai"
  },
  {
    "domain": "Spectrum.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Spectrum.ai"
  },
  {
    "domain": "Colorburst.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/Colorburst.ai"
  },
  {
    "domain": "Sunshower.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/Sunshower.ai"
  },
  {
    "domain": "Rainbow.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rainbow.ai"
  },
  {
    "domain": "Twinkle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Twinkle.ai"
  },
  {
    "domain": "Shimmer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Shimmer.ai"
  },
  {
    "domain": "Glitter.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Glitter.ai"
  },
  {
    "domain": "Radiance.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Radiance.ai"
  },
  {
    "domain": "Brilliance.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Brilliance.ai"
  },
  {
    "domain": "Gem.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Gem.ai"
  },
  {
    "domain": "Treasure.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Treasure.ai"
  },
  {
    "domain": "Goldmine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Goldmine.ai"
  },
  {
    "domain": "Shooting.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Shooting.ai"
  },
  {
    "domain": "Supernova.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Supernova.ai"
  },
  {
    "domain": "Comet.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Comet.ai"
  },
  {
    "domain": "Meteor.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Meteor.ai"
  },
  {
    "domain": "Blaze.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Blaze.ai"
  },
  {
    "domain": "Inferno.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Inferno.ai"
  },
  {
    "domain": "Bonfire.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Bonfire.ai"
  },
  {
    "domain": "Wildfire.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Wildfire.ai"
  },
  {
    "domain": "Tinder.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Tinder.ai"
  },
  {
    "domain": "Kindle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Kindle.ai"
  },
  {
    "domain": "Lightning.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Lightning.ai"
  },
  {
    "domain": "Zap.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Zap.ai"
  },
  {
    "domain": "Thunder.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Thunder.ai"
  },
  {
    "domain": "Zest.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Zest.ai"
  },
  {
    "domain": "Gusto.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Gusto.ai"
  },
  {
    "domain": "Verve.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Verve.ai"
  },
  {
    "domain": "Vigor.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Vigor.ai"
  },
  {
    "domain": "Vitality.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Vitality.ai"
  },
  {
    "domain": "Dynamo.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Dynamo.ai"
  },
  {
    "domain": "Thunder.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Thunder.ai"
  },
  {
    "domain": "Hurricane.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Hurricane.ai"
  },
  {
    "domain": "Cyclone.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Cyclone.ai"
  },
  {
    "domain": "Tempest.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Tempest.ai"
  },
  {
    "domain": "Storm.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Storm.ai"
  },
  {
    "domain": "Squall.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Squall.ai"
  },
  {
    "domain": "Monsoon.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Monsoon.ai"
  },
  {
    "domain": "Typhoon.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Typhoon.ai"
  },
  {
    "domain": "Tornado.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Tornado.ai"
  },
  {
    "domain": "Whirlwind.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Whirlwind.ai"
  },
  {
    "domain": "Gale.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Gale.ai"
  },
  {
    "domain": "Blizzard.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Blizzard.ai"
  },
  {
    "domain": "Avalanche.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Avalanche.ai"
  },
  {
    "domain": "Torrent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Torrent.ai"
  },
  {
    "domain": "Flood.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Flood.ai"
  },
  {
    "domain": "Deluge.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Deluge.ai"
  },
  {
    "domain": "Tsunami.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Tsunami.ai"
  },
  {
    "domain": "Wave.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Wave.ai"
  },
  {
    "domain": "Surge.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Surge.ai"
  },
  {
    "domain": "Undertow.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Undertow.ai"
  },
  {
    "domain": "Maelstrom.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Maelstrom.ai"
  },
  {
    "domain": "Vortex.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Vortex.ai"
  },
  {
    "domain": "Revolution.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Revolution.ai"
  },
  {
    "domain": "Innovation.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Innovation.ai"
  },
  {
    "domain": "Invention.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Invention.ai"
  },
  {
    "domain": "Creation.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Creation.ai"
  },
  {
    "domain": "Imagination.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Imagination.ai"
  },
  {
    "domain": "Ingenuity.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Ingenuity.ai"
  },
  {
    "domain": "Instinct.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Instinct.ai"
  },
  {
    "domain": "Intuition.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Intuition.ai"
  },
  {
    "domain": "Vision.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Vision.ai"
  },
  {
    "domain": "Foresight.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Foresight.ai"
  },
  {
    "domain": "Revelation.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Revelation.ai"
  },
  {
    "domain": "Epiphany.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Epiphany.ai"
  },
  {
    "domain": "Insight.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Insight.ai"
  },
  {
    "domain": "Discovery.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Discovery.ai"
  },
  {
    "domain": "Exploration.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Exploration.ai"
  },
  {
    "domain": "Curiosity.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Curiosity.ai"
  },
  {
    "domain": "Quest.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Quest.ai"
  },
  {
    "domain": "Adventure.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Adventure.ai"
  },
  {
    "domain": "Journey.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Journey.ai"
  },
  {
    "domain": "Voyage.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Voyage.ai"
  },
  {
    "domain": "Odyssey.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Odyssey.ai"
  },
  {
    "domain": "Expedition.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Expedition.ai"
  },
  {
    "domain": "Pioneer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Pioneer.ai"
  },
  {
    "domain": "Wanderer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Wanderer.ai"
  },
  {
    "domain": "Seeker.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Seeker.ai"
  },
  {
    "domain": "Dreamer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Dreamer.ai"
  },
  {
    "domain": "Stargazer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Stargazer.ai"
  },
  {
    "domain": "Innovator.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Innovator.ai"
  },
  {
    "domain": "Creator.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Creator.ai"
  },
  {
    "domain": "Visionary.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Visionary.ai"
  },
  {
    "domain": "Luminary.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Luminary.ai"
  },
  {
    "domain": "Genius.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Genius.ai"
  },
  {
    "domain": "Prodigy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Prodigy.ai"
  },
  {
    "domain": "Maverick.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Maverick.ai"
  },
  {
    "domain": "Rebel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rebel.ai"
  },
  {
    "domain": "Leader.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Leader.ai"
  },
  {
    "domain": "Trailblazer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Trailblazer.ai"
  },
  {
    "domain": "Founder.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Founder.ai"
  },
  {
    "domain": "Bright.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Bright.ai"
  },
  {
    "domain": "Rising.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rising.ai"
  },
  {
    "domain": "Shooting.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Shooting.ai"
  },
  {
    "domain": "Shining.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Shining.ai"
  },
  {
    "domain": "Guiding.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Guiding.ai"
  },
  {
    "domain": "Beacon.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Beacon.ai"
  },
  {
    "domain": "Torch.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Torch.ai"
  },
  {
    "domain": "Spark.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Spark.ai"
  },
  {
    "domain": "Catalyst.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Catalyst.ai"
  },
  {
    "domain": "Change.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Change.ai"
  },
  {
    "domain": "Disruptor.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Disruptor.ai"
  },
  {
    "domain": "Game.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Game.ai"
  },
  {
    "domain": "Pacesetter.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Pacesetter.ai"
  },
  {
    "domain": "Frontier.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Frontier.ai"
  },
  {
    "domain": "Uncharted.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Uncharted.ai"
  },
  {
    "domain": "Unknown.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Unknown.ai"
  },
  {
    "domain": "Mystery.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Mystery.ai"
  },
  {
    "domain": "Enigma.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Enigma.ai"
  },
  {
    "domain": "Riddle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Riddle.ai"
  },
  {
    "domain": "Paradox.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Paradox.ai"
  },
  {
    "domain": "Conundrum.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Conundrum.ai"
  },
  {
    "domain": "Cipher.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Cipher.ai"
  },
  {
    "domain": "Puzzle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Puzzle.ai"
  },
  {
    "domain": "Mystic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Mystic.ai"
  },
  {
    "domain": "Occult.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Occult.ai"
  },
  {
    "domain": "Esoteric.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Esoteric.ai"
  },
  {
    "domain": "Arcane.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Arcane.ai"
  },
  {
    "domain": "Obscure.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Obscure.ai"
  },
  {
    "domain": "Cryptic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Cryptic.ai"
  },
  {
    "domain": "Veil.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Veil.ai"
  },
  {
    "domain": "Mask.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Mask.ai"
  },
  {
    "domain": "Facade.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Facade.ai"
  },
  {
    "domain": "Charade.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Charade.ai"
  },
  {
    "domain": "Mirage.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Mirage.ai"
  },
  {
    "domain": "Illusion.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Illusion.ai"
  },
  {
    "domain": "Sleight.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Sleight.ai"
  },
  {
    "domain": "Prestige.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Prestige.ai"
  },
  {
    "domain": "Sorcery.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Sorcery.ai"
  },
  {
    "domain": "Wizardry.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Wizardry.ai"
  },
  {
    "domain": "Magic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Magic.ai"
  },
  {
    "domain": "Spell.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Spell.ai"
  },
  {
    "domain": "Abracadabra.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Abracadabra.ai"
  },
  {
    "domain": "Hocus.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Hocus.ai"
  },
  {
    "domain": "Alakazam.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Alakazam.ai"
  },
  {
    "domain": "Metamorphosis.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Metamorphosis.ai"
  },
  {
    "domain": "Transform.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Transform.ai"
  },
  {
    "domain": "Evolve.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Evolve.ai"
  },
  {
    "domain": "Ascend.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Ascend.ai"
  },
  {
    "domain": "Transcend.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Transcend.ai"
  },
  {
    "domain": "Enlighten.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Enlighten.ai"
  },
  {
    "domain": "Awaken.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Awaken.ai"
  },
  {
    "domain": "Liberate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Liberate.ai"
  },
  {
    "domain": "Empower.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Empower.ai"
  },
  {
    "domain": "Inspire.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Inspire.ai"
  },
  {
    "domain": "Motivate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Motivate.ai"
  },
  {
    "domain": "Energize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Energize.ai"
  },
  {
    "domain": "Invigorate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Invigorate.ai"
  },
  {
    "domain": "Revitalize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Revitalize.ai"
  },
  {
    "domain": "Restore.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Restore.ai"
  },
  {
    "domain": "Renew.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Renew.ai"
  },
  {
    "domain": "Refresh.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Refresh.ai"
  },
  {
    "domain": "Rejuvenate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rejuvenate.ai"
  },
  {
    "domain": "Resuscitate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/Resuscitate.ai"
  },
  {
    "domain": "Revive.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Revive.ai"
  },
  {
    "domain": "Rouse.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rouse.ai"
  },
  {
    "domain": "Kindle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Kindle.ai"
  },
  {
    "domain": "Ignite.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Ignite.ai"
  },
  {
    "domain": "Inflame.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/Inflame.ai"
  },
  {
    "domain": "Fire.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Fire.ai"
  },
  {
    "domain": "Spark.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Spark.ai"
  },
  {
    "domain": "Fuel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Fuel.ai"
  },
  {
    "domain": "Stoke.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Stoke.ai"
  },
  {
    "domain": "Stir.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Stir.ai"
  },
  {
    "domain": "Galvanize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Galvanize.ai"
  },
  {
    "domain": "Electrify.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Electrify.ai"
  },
  {
    "domain": "Shock.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Shock.ai"
  },
  {
    "domain": "Jolt.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Jolt.ai"
  },
  {
    "domain": "Activate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Activate.ai"
  },
  {
    "domain": "Animate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Animate.ai"
  },
  {
    "domain": "Bring.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Bring.ai"
  },
  {
    "domain": "Give.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Give.ai"
  },
  {
    "domain": "Take.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Take.ai"
  },
  {
    "domain": "Insightful.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Insightful.ai"
  },
  {
    "domain": "Brilliant.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Brilliant.ai"
  },
  {
    "domain": "Wise.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Wise.ai"
  },
  {
    "domain": "Genius.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Genius.ai"
  },
  {
    "domain": "Intelligent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Intelligent.ai"
  },
  {
    "domain": "Smart.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Smart.ai"
  },
  {
    "domain": "Invent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Invent.ai"
  },
  {
    "domain": "Creative.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Creative.ai"
  },
  {
    "domain": "Imagine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Imagine.ai"
  },
  {
    "domain": "Innovate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Innovate.ai"
  },
  {
    "domain": "Original.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Original.ai"
  },
  {
    "domain": "Novel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Novel.ai"
  },
  {
    "domain": "Pioneer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Pioneer.ai"
  },
  {
    "domain": "Revolution.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Revolution.ai"
  },
  {
    "domain": "Visionary.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Visionary.ai"
  },
  {
    "domain": "Futuristic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Futuristic.ai"
  },
  {
    "domain": "Forward.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Forward.ai"
  },
  {
    "domain": "Lead.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Lead.ai"
  },
  {
    "domain": "CuttingEdge.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/CuttingEdge.ai"
  },
  {
    "domain": "AvantGarde.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/AvantGarde.ai"
  },
  {
    "domain": "Advanced.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Advanced.ai"
  },
  {
    "domain": "StateOfTheArt.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/StateOfTheArt.ai"
  },
  {
    "domain": "Modern.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Modern.ai"
  },
  {
    "domain": "Contemporary.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Contemporary.ai"
  },
  {
    "domain": "Current.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Current.ai"
  },
  {
    "domain": "Latest.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Latest.ai"
  },
  {
    "domain": "Recent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Recent.ai"
  },
  {
    "domain": "Fresh.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Fresh.ai"
  },
  {
    "domain": "New.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/New.ai"
  },
  {
    "domain": "Unique.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Unique.ai"
  },
  {
    "domain": "OneOfAKind.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/OneOfAKind.ai"
  },
  {
    "domain": "Different.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Different.ai"
  },
  {
    "domain": "Distinct.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Distinct.ai"
  },
  {
    "domain": "Uncommon.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Uncommon.ai"
  },
  {
    "domain": "Rare.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rare.ai"
  },
  {
    "domain": "Exclusive.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Exclusive.ai"
  },
  {
    "domain": "Exceptional.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Exceptional.ai"
  },
  {
    "domain": "Extraordinary.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Extraordinary.ai"
  },
  {
    "domain": "Outstanding.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Outstanding.ai"
  },
  {
    "domain": "Superb.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Superb.ai"
  },
  {
    "domain": "Stellar.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Stellar.ai"
  },
  {
    "domain": "Skillful.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Skillful.ai"
  },
  {
    "domain": "Masterful.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Masterful.ai"
  },
  {
    "domain": "Expert.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Expert.ai"
  },
  {
    "domain": "Specialist.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Specialist.ai"
  },
  {
    "domain": "Professional.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Professional.ai"
  },
  {
    "domain": "WorldClass.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/WorldClass.ai"
  },
  {
    "domain": "Renown.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Renown.ai"
  },
  {
    "domain": "Celebrate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Celebrate.ai"
  },
  {
    "domain": "Fame.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Fame.ai"
  },
  {
    "domain": "Esteem.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Esteem.ai"
  },
  {
    "domain": "Reputable.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Reputable.ai"
  },
  {
    "domain": "Prominent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Prominent.ai"
  },
  {
    "domain": "Eminent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Eminent.ai"
  },
  {
    "domain": "Distinguish.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Distinguish.ai"
  },
  {
    "domain": "Prestigious.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Prestigious.ai"
  },
  {
    "domain": "Elite.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Elite.ai"
  },
  {
    "domain": "Refine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Refine.ai"
  },
  {
    "domain": "Culture.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Culture.ai"
  },
  {
    "domain": "Sophisticate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Sophisticate.ai"
  },
  {
    "domain": "Discern.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Discern.ai"
  },
  {
    "domain": "Select.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Select.ai"
  },
  {
    "domain": "Eclectic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Eclectic.ai"
  },
  {
    "domain": "Cosmopolitan.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Cosmopolitan.ai"
  },
  {
    "domain": "Progressive.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Progressive.ai"
  },
  {
    "domain": "Evolve.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Evolve.ai"
  },
  {
    "domain": "Develop.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Develop.ai"
  },
  {
    "domain": "Emerge.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Emerge.ai"
  },
  {
    "domain": "Mature.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Mature.ai"
  },
  {
    "domain": "Promise.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Promise.ai"
  },
  {
    "domain": "Bud.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Bud.ai"
  },
  {
    "domain": "Thrive.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Thrive.ai"
  },
  {
    "domain": "Flourish.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Flourish.ai"
  },
  {
    "domain": "Prosper.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Prosper.ai"
  },
  {
    "domain": "Grow.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Grow.ai"
  },
  {
    "domain": "Expand.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Expand.ai"
  },
  {
    "domain": "Advance.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Advance.ai"
  },
  {
    "domain": "Improve.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Improve.ai"
  },
  {
    "domain": "Optimize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Optimize.ai"
  },
  {
    "domain": "Enhance.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Enhance.ai"
  },
  {
    "domain": "Upgrade.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Upgrade.ai"
  },
  {
    "domain": "Transform.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Transform.ai"
  },
  {
    "domain": "Modernize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Modernize.ai"
  },
  {
    "domain": "Innovate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Innovate.ai"
  },
  {
    "domain": "Create.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Create.ai"
  },
  {
    "domain": "Design.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Design.ai"
  },
  {
    "domain": "Engineer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Engineer.ai"
  },
  {
    "domain": "Construct.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Construct.ai"
  },
  {
    "domain": "Build.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Build.ai"
  },
  {
    "domain": "Produce.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Produce.ai"
  },
  {
    "domain": "Generate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Generate.ai"
  },
  {
    "domain": "Formulate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Formulate.ai"
  },
  {
    "domain": "Fabricate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Fabricate.ai"
  },
  {
    "domain": "Manufacture.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Manufacture.ai"
  },
  {
    "domain": "Craft.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Craft.ai"
  },
  {
    "domain": "Tailor.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Tailor.ai"
  },
  {
    "domain": "Customize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Customize.ai"
  },
  {
    "domain": "Personalize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Personalize.ai"
  },
  {
    "domain": "Specialize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Specialize.ai"
  },
  {
    "domain": "Focus.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Focus.ai"
  },
  {
    "domain": "Concentrate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Concentrate.ai"
  },
  {
    "domain": "Centralize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Centralize.ai"
  },
  {
    "domain": "Streamline.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Streamline.ai"
  },
  {
    "domain": "Simplify.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Simplify.ai"
  },
  {
    "domain": "Refine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Refine.ai"
  },
  {
    "domain": "Perfect.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Perfect.ai"
  },
  {
    "domain": "Polish.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Polish.ai"
  },
  {
    "domain": "Enrich.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Enrich.ai"
  },
  {
    "domain": "Augment.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Augment.ai"
  },
  {
    "domain": "Boost.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Boost.ai"
  },
  {
    "domain": "Elevate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Elevate.ai"
  },
  {
    "domain": "Enhance.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Enhance.ai"
  },
  {
    "domain": "Magnify.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Magnify.ai"
  },
  {
    "domain": "Maximize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Maximize.ai"
  },
  {
    "domain": "Optimize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Optimize.ai"
  },
  {
    "domain": "Heighten.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Heighten.ai"
  },
  {
    "domain": "Intensify.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Intensify.ai"
  },
  {
    "domain": "Deepen.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Deepen.ai"
  },
  {
    "domain": "Strengthen.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Strengthen.ai"
  },
  {
    "domain": "Fortify.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Fortify.ai"
  },
  {
    "domain": "Bolster.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Bolster.ai"
  },
  {
    "domain": "Reinforce.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Reinforce.ai"
  },
  {
    "domain": "Invigorate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Invigorate.ai"
  },
  {
    "domain": "Energize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Energize.ai"
  },
  {
    "domain": "Animate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Animate.ai"
  },
  {
    "domain": "Stimulate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Stimulate.ai"
  },
  {
    "domain": "Galvanize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Galvanize.ai"
  },
  {
    "domain": "Activate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Activate.ai"
  },
  {
    "domain": "Accelerate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Accelerate.ai"
  },
  {
    "domain": "Advance.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Advance.ai"
  },
  {
    "domain": "Promote.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Promote.ai"
  },
  {
    "domain": "Propel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Propel.ai"
  },
  {
    "domain": "Drive.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Drive.ai"
  },
  {
    "domain": "Motivate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Motivate.ai"
  },
  {
    "domain": "Inspire.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Inspire.ai"
  },
  {
    "domain": "Excite.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Excite.ai"
  },
  {
    "domain": "Captivate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Captivate.ai"
  },
  {
    "domain": "Engage.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Engage.ai"
  },
  {
    "domain": "Enthrall.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Enthrall.ai"
  },
  {
    "domain": "Grip.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Grip.ai"
  },
  {
    "domain": "Rivet.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rivet.ai"
  },
  {
    "domain": "Mesmerize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Mesmerize.ai"
  },
  {
    "domain": "Hypnotize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Hypnotize.ai"
  },
  {
    "domain": "Spellbind.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Spellbind.ai"
  },
  {
    "domain": "Entrance.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Entrance.ai"
  },
  {
    "domain": "Enchant.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Enchant.ai"
  },
  {
    "domain": "Bewitch.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Bewitch.ai"
  },
  {
    "domain": "Allure.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Allure.ai"
  },
  {
    "domain": "Appeal.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Appeal.ai"
  },
  {
    "domain": "Fetch.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Fetch.ai"
  },
  {
    "domain": "Charm.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Charm.ai"
  },
  {
    "domain": "Magnetize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Magnetize.ai"
  },
  {
    "domain": "Attract.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Attract.ai"
  },
  {
    "domain": "Dazzle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Dazzle.ai"
  },
  {
    "domain": "Stun.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Stun.ai"
  },
  {
    "domain": "Strike.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Strike.ai"
  },
  {
    "domain": "Splendid.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Splendid.ai"
  },
  {
    "domain": "Magnificent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Magnificent.ai"
  },
  {
    "domain": "Majestic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Majestic.ai"
  },
  {
    "domain": "Grand.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Grand.ai"
  },
  {
    "domain": "Impose.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/Impose.ai"
  },
  {
    "domain": "Impress.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Impress.ai"
  },
  {
    "domain": "Breathtake.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/Breathtake.ai"
  },
  {
    "domain": "AweInspire.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/AweInspire.ai"
  },
  {
    "domain": "Wonder.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Wonder.ai"
  },
  {
    "domain": "Marvel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Marvel.ai"
  },
  {
    "domain": "Amaze.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Amaze.ai"
  },
  {
    "domain": "Astonish.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Astonish.ai"
  },
  {
    "domain": "Astound.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Astound.ai"
  },
  {
    "domain": "Stupendous.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Stupendous.ai"
  },
  {
    "domain": "Spectacular.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Spectacular.ai"
  },
  {
    "domain": "Sensational.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Sensational.ai"
  },
  {
    "domain": "Miraculous.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Miraculous.ai"
  },
  {
    "domain": "Extraordinary.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Extraordinary.ai"
  },
  {
    "domain": "Unbelieve.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/Unbelieve.ai"
  },
  {
    "domain": "Inconceive.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/Inconceive.ai"
  },
  {
    "domain": "Unimagine.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/Unimagine.ai"
  },
  {
    "domain": "MindBlow.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/MindBlow.ai"
  },
  {
    "domain": "JawDrop.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/JawDrop.ai"
  },
  {
    "domain": "EyePop.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/EyePop.ai"
  },
  {
    "domain": "Showstop.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/Showstop.ai"
  },
  {
    "domain": "Mesmerize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Mesmerize.ai"
  },
  {
    "domain": "Ravish.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/Ravish.ai"
  },
  {
    "domain": "Captivate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Captivate.ai"
  },
  {
    "domain": "Enthrall.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Enthrall.ai"
  },
  {
    "domain": "Enchant.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Enchant.ai"
  },
  {
    "domain": "Enrapture.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Enrapture.ai"
  },
  {
    "domain": "Grip.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Grip.ai"
  },
  {
    "domain": "Rivet.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rivet.ai"
  },
  {
    "domain": "Thrill.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Thrill.ai"
  },
  {
    "domain": "Exhilarate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Exhilarate.ai"
  },
  {
    "domain": "Electrify.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Electrify.ai"
  },
  {
    "domain": "Rouse.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rouse.ai"
  },
  {
    "domain": "Animate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Animate.ai"
  },
  {
    "domain": "Inspire.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Inspire.ai"
  },
  {
    "domain": "Uplift.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Uplift.ai"
  },
  {
    "domain": "Revitalize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Revitalize.ai"
  },
  {
    "domain": "Rejuvenate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Rejuvenate.ai"
  },
  {
    "domain": "Refresh.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Refresh.ai"
  },
  {
    "domain": "Invigorate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Invigorate.ai"
  },
  {
    "domain": "Stimulate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Stimulate.ai"
  },
  {
    "domain": "Energize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Energize.ai"
  },
  {
    "domain": "Vitalize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Vitalize.ai"
  },
  {
    "domain": "Exhilarate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Exhilarate.ai"
  },
  {
    "domain": "Elate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Elate.ai"
  },
  {
    "domain": "apple.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/apple.ai"
  },
  {
    "domain": "saudiaramco.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/saudiaramco.ai"
  },
  {
    "domain": "microsoft.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/microsoft.ai"
  },
  {
    "domain": "abc.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/abc.ai"
  },
  {
    "domain": "amazon.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/amazon.ai"
  },
  {
    "domain": "berkshirehathaway.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/berkshirehathaway.ai"
  },
  {
    "domain": "unitedhealthgroup.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/unitedhealthgroup.ai"
  },
  {
    "domain": "jnj.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/jnj.ai"
  },
  {
    "domain": "corporate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/corporate.ai"
  },
  {
    "domain": "visa.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/visa.ai"
  },
  {
    "domain": "tencent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/tencent.ai"
  },
  {
    "domain": "tesla.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/tesla.ai"
  },
  {
    "domain": "tsmc.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/tsmc.ai"
  },
  {
    "domain": "walmart.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/walmart.ai"
  },
  {
    "domain": "jpmorganchase.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/jpmorganchase.ai"
  },
  {
    "domain": "nvidia.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/nvidia.ai"
  },
  {
    "domain": "lvmh.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/lvmh.ai"
  },
  {
    "domain": "pg.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/pg.ai"
  },
  {
    "domain": "lilly.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/lilly.ai"
  },
  {
    "domain": "chevron.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/chevron.ai"
  },
  {
    "domain": "mastercard.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mastercard.ai"
  },
  {
    "domain": "homedepot.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/homedepot.ai"
  },
  {
    "domain": "nestle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/nestle.ai"
  },
  {
    "domain": "facebook.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/facebook.ai"
  },
  {
    "domain": "samsung.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/samsung.ai"
  },
  {
    "domain": "novonordisk.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/novonordisk.ai"
  },
  {
    "domain": "pfizer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/pfizer.ai"
  },
  {
    "domain": "abbvie.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/abbvie.ai"
  },
  {
    "domain": "merck.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/merck.ai"
  },
  {
    "domain": "tata.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/tata.ai"
  },
  {
    "domain": "coca-colacompany.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/coca-colacompany.ai"
  },
  {
    "domain": "roche.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/roche.ai"
  },
  {
    "domain": "bankofamerica.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bankofamerica.ai"
  },
  {
    "domain": "pepsico.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/pepsico.ai"
  },
  {
    "domain": "broadcom.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/broadcom.ai"
  },
  {
    "domain": "alibaba.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/alibaba.ai"
  },
  {
    "domain": "asml.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/asml.ai"
  },
  {
    "domain": "oracle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/oracle.ai"
  },
  {
    "domain": "thermofisher.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/thermofisher.ai"
  },
  {
    "domain": "astrazeneca.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/astrazeneca.ai"
  },
  {
    "domain": "icbc.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/icbc.ai"
  },
  {
    "domain": "ril.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ril.ai"
  },
  {
    "domain": "prosus.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/prosus.ai"
  },
  {
    "domain": "costco.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/costco.ai"
  },
  {
    "domain": "shell.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/shell.ai"
  },
  {
    "domain": "mcdonalds.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mcdonalds.ai"
  },
  {
    "domain": "novartis.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/novartis.ai"
  },
  {
    "domain": "cisco.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cisco.ai"
  },
  {
    "domain": "loreal.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/loreal.ai"
  },
  {
    "domain": "danaher.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/danaher.ai"
  },
  {
    "domain": "abbott.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/abbott.ai"
  },
  {
    "domain": "toyota-global.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/toyota-global.ai"
  },
  {
    "domain": "nike.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/nike.ai"
  },
  {
    "domain": "t-mobile.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/t-mobile.ai"
  },
  {
    "domain": "accenture.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/accenture.ai"
  },
  {
    "domain": "nexteraenergy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/nexteraenergy.ai"
  },
  {
    "domain": "hermes.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/hermes.ai"
  },
  {
    "domain": "the-linde-group.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/the-linde-group.ai"
  },
  {
    "domain": "verizon.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/verizon.ai"
  },
  {
    "domain": "thewaltdisneycompany.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/thewaltdisneycompany.ai"
  },
  {
    "domain": "pmi.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/pmi.ai"
  },
  {
    "domain": "adobe.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/adobe.ai"
  },
  {
    "domain": "totalenergies.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/totalenergies.ai"
  },
  {
    "domain": "bhp.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bhp.ai"
  },
  {
    "domain": "wellsfargo.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/wellsfargo.ai"
  },
  {
    "domain": "bms.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bms.ai"
  },
  {
    "domain": "ups.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ups.ai"
  },
  {
    "domain": "schwab.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/schwab.ai"
  },
  {
    "domain": "corporate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/corporate.ai"
  },
  {
    "domain": "en.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/en.ai"
  },
  {
    "domain": "ti.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ti.ai"
  },
  {
    "domain": "utc.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/utc.ai"
  },
  {
    "domain": "conocophillips.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/conocophillips.ai"
  },
  {
    "domain": "morganstanley.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/morganstanley.ai"
  },
  {
    "domain": "meituan.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/meituan.ai"
  },
  {
    "domain": "chinamobileltd.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/chinamobileltd.ai"
  },
  {
    "domain": "tcs.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/tcs.ai"
  },
  {
    "domain": "honeywell.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/honeywell.ai"
  },
  {
    "domain": "abchina.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/abchina.ai"
  },
  {
    "domain": "amgen.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/amgen.ai"
  },
  {
    "domain": "atlbattery.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/atlbattery.ai"
  },
  {
    "domain": "cmbchina.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cmbchina.ai"
  },
  {
    "domain": "netflix.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/netflix.ai"
  },
  {
    "domain": "dior.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/dior.ai"
  },
  {
    "domain": "rbcroyalbank.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/rbcroyalbank.ai"
  },
  {
    "domain": "att.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/att.ai"
  },
  {
    "domain": "aia.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/aia.ai"
  },
  {
    "domain": "deere.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/deere.ai"
  },
  {
    "domain": "salesforce.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/salesforce.ai"
  },
  {
    "domain": "unilever.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/unilever.ai"
  },
  {
    "domain": "up.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/up.ai"
  },
  {
    "domain": "ibm.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ibm.ai"
  },
  {
    "domain": "lockheedmartin.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/lockheedmartin.ai"
  },
  {
    "domain": "caterpillar.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/caterpillar.ai"
  },
  {
    "domain": "qualcomm.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/qualcomm.ai"
  },
  {
    "domain": "boc.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/boc.ai"
  },
  {
    "domain": "hsbc.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/hsbc.ai"
  },
  {
    "domain": "cvshealth.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cvshealth.ai"
  },
  {
    "domain": "elevancehealth.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/elevancehealth.ai"
  },
  {
    "domain": "lowes.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/lowes.ai"
  },
  {
    "domain": "sanofi.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sanofi.ai"
  },
  {
    "domain": "sap.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sap.ai"
  },
  {
    "domain": "chinalife.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/chinalife.ai"
  },
  {
    "domain": "ab-inbev.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/ab-inbev.ai"
  },
  {
    "domain": "pingan.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/pingan.ai"
  },
  {
    "domain": "commbank.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/commbank.ai"
  },
  {
    "domain": "td.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/td.ai"
  },
  {
    "domain": "goldmansachs.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/goldmansachs.ai"
  },
  {
    "domain": "equinor.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/equinor.ai"
  },
  {
    "domain": "riotinto.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/riotinto.ai"
  },
  {
    "domain": "starbucks.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/starbucks.ai"
  },
  {
    "domain": "boeing.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/boeing.ai"
  },
  {
    "domain": "youtube.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/youtube.ai"
  },
  {
    "domain": "americanexpress.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/americanexpress.ai"
  },
  {
    "domain": "hdfcbank.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/hdfcbank.ai"
  },
  {
    "domain": "spglobal.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/spglobal.ai"
  },
  {
    "domain": "siemens.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/siemens.ai"
  },
  {
    "domain": "intuit.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/intuit.ai"
  },
  {
    "domain": "intel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/intel.ai"
  },
  {
    "domain": "gilead.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/gilead.ai"
  },
  {
    "domain": "m.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/m.ai"
  },
  {
    "domain": "lindt-spruengli.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/lindt-spruengli.ai"
  },
  {
    "domain": "blackrock.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/blackrock.ai"
  },
  {
    "domain": "bp.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bp.ai"
  },
  {
    "domain": "amd.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/amd.ai"
  },
  {
    "domain": "prologis.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/prologis.ai"
  },
  {
    "domain": "medtronic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/medtronic.ai"
  },
  {
    "domain": "diageo.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/diageo.ai"
  },
  {
    "domain": "cigna.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cigna.ai"
  },
  {
    "domain": "wuliangye.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/wuliangye.ai"
  },
  {
    "domain": "telekom.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/telekom.ai"
  },
  {
    "domain": "statefarm.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/statefarm.ai"
  },
  {
    "domain": "adp.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/adp.ai"
  },
  {
    "domain": "edison.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/edison.ai"
  },
  {
    "domain": "nttdocomo.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/nttdocomo.ai"
  },
  {
    "domain": "americantower.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/americantower.ai"
  },
  {
    "domain": "global.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/global.ai"
  },
  {
    "domain": "sony.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sony.ai"
  },
  {
    "domain": "keyence.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/keyence.ai"
  },
  {
    "domain": "airbus.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/airbus.ai"
  },
  {
    "domain": "investor.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/investor.ai"
  },
  {
    "domain": "csl.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/csl.ai"
  },
  {
    "domain": "intuitive.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/intuitive.ai"
  },
  {
    "domain": "byd.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/byd.ai"
  },
  {
    "domain": "stryker.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/stryker.ai"
  },
  {
    "domain": "tjx.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/tjx.ai"
  },
  {
    "domain": "mondelezinternational.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mondelezinternational.ai"
  },
  {
    "domain": "kochind.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/kochind.ai"
  },
  {
    "domain": "bytedance.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bytedance.ai"
  },
  {
    "domain": "chubb.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/chubb.ai"
  },
  {
    "domain": "bat.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bat.ai"
  },
  {
    "domain": "ge.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ge.ai"
  },
  {
    "domain": "jd.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/jd.ai"
  },
  {
    "domain": "mufg.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mufg.ai"
  },
  {
    "domain": "allianz.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/allianz.ai"
  },
  {
    "domain": "glencore.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/glencore.ai"
  },
  {
    "domain": "elcompanies.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/elcompanies.ai"
  },
  {
    "domain": "citigroup.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/citigroup.ai"
  },
  {
    "domain": "analog.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/analog.ai"
  },
  {
    "domain": "merckgroup.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/merckgroup.ai"
  },
  {
    "domain": "altria.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/altria.ai"
  },
  {
    "domain": "northropgrumman.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/northropgrumman.ai"
  },
  {
    "domain": "inditex.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/inditex.ai"
  },
  {
    "domain": "mmc.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mmc.ai"
  },
  {
    "domain": "appliedmaterials.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/appliedmaterials.ai"
  },
  {
    "domain": "cn.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cn.ai"
  },
  {
    "domain": "luxottica.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/luxottica.ai"
  },
  {
    "domain": "bosch.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bosch.ai"
  },
  {
    "domain": "enbridge.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/enbridge.ai"
  },
  {
    "domain": "duke-energy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/duke-energy.ai"
  },
  {
    "domain": "regeneron.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/regeneron.ai"
  },
  {
    "domain": "alrajhibank.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/alrajhibank.ai"
  },
  {
    "domain": "paypal.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/paypal.ai"
  },
  {
    "domain": "southerncompany.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/southerncompany.ai"
  },
  {
    "domain": "schneider-electric.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/schneider-electric.ai"
  },
  {
    "domain": "vale.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/vale.ai"
  },
  {
    "domain": "audi.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/audi.ai"
  },
  {
    "domain": "deloitte.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/deloitte.ai"
  },
  {
    "domain": "servicenow.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/servicenow.ai"
  },
  {
    "domain": "eogresources.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/eogresources.ai"
  },
  {
    "domain": "modernatx.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/modernatx.ai"
  },
  {
    "domain": "cargill.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cargill.ai"
  },
  {
    "domain": "bookingholdings.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bookingholdings.ai"
  },
  {
    "domain": "progressive.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/progressive.ai"
  },
  {
    "domain": "icicibank.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/icicibank.ai"
  },
  {
    "domain": "infosys.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/infosys.ai"
  },
  {
    "domain": "slb.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/slb.ai"
  },
  {
    "domain": "csec.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/csec.ai"
  },
  {
    "domain": "whatsapp.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/whatsapp.ai"
  },
  {
    "domain": "airliquide.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/airliquide.ai"
  },
  {
    "domain": "vrtx.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/vrtx.ai"
  },
  {
    "domain": "hul.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/hul.ai"
  },
  {
    "domain": "bd.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bd.ai"
  },
  {
    "domain": "gsk.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/gsk.ai"
  },
  {
    "domain": "volkswagenag.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/volkswagenag.ai"
  },
  {
    "domain": "swatchgroup.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/swatchgroup.ai"
  },
  {
    "domain": "richemont.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/richemont.ai"
  },
  {
    "domain": "zurich.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/zurich.ai"
  },
  {
    "domain": "iberdrola.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/iberdrola.ai"
  },
  {
    "domain": "sinopecgroup.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/sinopecgroup.ai"
  },
  {
    "domain": "group.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/group.ai"
  },
  {
    "domain": "cpr.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cpr.ai"
  },
  {
    "domain": "pwc.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/pwc.ai"
  },
  {
    "domain": "daimler.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/daimler.ai"
  },
  {
    "domain": "airproducts.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/airproducts.ai"
  },
  {
    "domain": "spectrum.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/spectrum.ai"
  },
  {
    "domain": "petrobras.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/petrobras.ai"
  },
  {
    "domain": "sberbank.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sberbank.ai"
  },
  {
    "domain": "sabic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sabic.ai"
  },
  {
    "domain": "itw.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/itw.ai"
  },
  {
    "domain": "allergan.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/allergan.ai"
  },
  {
    "domain": "gd.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/gd.ai"
  },
  {
    "domain": "publix.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/publix.ai"
  },
  {
    "domain": "hcahealthcare.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/hcahealthcare.ai"
  },
  {
    "domain": "zoetis.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/zoetis.ai"
  },
  {
    "domain": "bca.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bca.ai"
  },
  {
    "domain": "kddi.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/kddi.ai"
  },
  {
    "domain": "3m.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/3m.ai"
  },
  {
    "domain": "axa.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/axa.ai"
  },
  {
    "domain": "colgatepalmolive.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/colgatepalmolive.ai"
  },
  {
    "domain": "usbank.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/usbank.ai"
  },
  {
    "domain": "bostonscientific.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bostonscientific.ai"
  },
  {
    "domain": "target.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/target.ai"
  },
  {
    "domain": "jio.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/jio.ai"
  },
  {
    "domain": "cits.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/cits.ai"
  },
  {
    "domain": "csx.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/csx.ai"
  },
  {
    "domain": "wm.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/wm.ai"
  },
  {
    "domain": "humana.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/humana.ai"
  },
  {
    "domain": "dbs.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/dbs.ai"
  },
  {
    "domain": "walmex.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/walmex.ai"
  },
  {
    "domain": "onlinesbi.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/onlinesbi.ai"
  },
  {
    "domain": "nab.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/nab.ai"
  },
  {
    "domain": "fiserv.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/fiserv.ai"
  },
  {
    "domain": "nongfuspring.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/nongfuspring.ai"
  },
  {
    "domain": "rosneft.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/rosneft.ai"
  },
  {
    "domain": "bmo.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bmo.ai"
  },
  {
    "domain": "softbank.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/softbank.ai"
  },
  {
    "domain": "sherwin-williams.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/sherwin-williams.ai"
  },
  {
    "domain": "pnc.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/pnc.ai"
  },
  {
    "domain": "cnoocltd.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/cnoocltd.ai"
  },
  {
    "domain": "eaton.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/eaton.ai"
  },
  {
    "domain": "cmegroup.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/cmegroup.ai"
  },
  {
    "domain": "aon.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/aon.ai"
  },
  {
    "domain": "daiichisankyo.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/daiichisankyo.ai"
  },
  {
    "domain": "cnrl.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/cnrl.ai"
  },
  {
    "domain": "kering.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/kering.ai"
  },
  {
    "domain": "fastretailing.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/fastretailing.ai"
  },
  {
    "domain": "equinix.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/equinix.ai"
  },
  {
    "domain": "activisionblizzard.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/activisionblizzard.ai"
  },
  {
    "domain": "crowncastle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/crowncastle.ai"
  },
  {
    "domain": "verbund.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/verbund.ai"
  },
  {
    "domain": "ubs.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ubs.ai"
  },
  {
    "domain": "americamovil.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/americamovil.ai"
  },
  {
    "domain": "hdfc.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/hdfc.ai"
  },
  {
    "domain": "bmwgroup.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/bmwgroup.ai"
  },
  {
    "domain": "scotiabank.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/scotiabank.ai"
  },
  {
    "domain": "oxy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/oxy.ai"
  },
  {
    "domain": "psbc.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/psbc.ai"
  },
  {
    "domain": "ey.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ey.ai"
  },
  {
    "domain": "intercontinentalexchange.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/intercontinentalexchange.ai"
  },
  {
    "domain": "nscorp.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/nscorp.ai"
  },
  {
    "domain": "alahli.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/alahli.ai"
  },
  {
    "domain": "metlife.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/metlife.ai"
  },
  {
    "domain": "novatek.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/novatek.ai"
  },
  {
    "domain": "new.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/new.ai"
  },
  {
    "domain": "bbt.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bbt.ai"
  },
  {
    "domain": "vinci.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/vinci.ai"
  },
  {
    "domain": "lamresearch.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/lamresearch.ai"
  },
  {
    "domain": "emerson.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/emerson.ai"
  },
  {
    "domain": "atlascopco.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/atlascopco.ai"
  },
  {
    "domain": "enel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/enel.ai"
  },
  {
    "domain": "aldi.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/aldi.ai"
  },
  {
    "domain": "investorab.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/investorab.ai"
  },
  {
    "domain": "dollargeneral.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/dollargeneral.ai"
  },
  {
    "domain": "corporate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/corporate.ai"
  },
  {
    "domain": "hkex.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/hkex.ai"
  },
  {
    "domain": "smfg.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/smfg.ai"
  },
  {
    "domain": "westpac.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/westpac.ai"
  },
  {
    "domain": "blackstone.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/blackstone.ai"
  },
  {
    "domain": "mindray.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mindray.ai"
  },
  {
    "domain": "micron.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/micron.ai"
  },
  {
    "domain": "haitian-food.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/haitian-food.ai"
  },
  {
    "domain": "airtel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/airtel.ai"
  },
  {
    "domain": "fcx.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/fcx.ai"
  },
  {
    "domain": "pxd.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/pxd.ai"
  },
  {
    "domain": "aig.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/aig.ai"
  },
  {
    "domain": "mckesson.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mckesson.ai"
  },
  {
    "domain": "thomsonreuters.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/thomsonreuters.ai"
  },
  {
    "domain": "marathonpetroleum.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/marathonpetroleum.ai"
  },
  {
    "domain": "kla-tencor.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/kla-tencor.ai"
  },
  {
    "domain": "relx.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/relx.ai"
  },
  {
    "domain": "safran-group.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/safran-group.ai"
  },
  {
    "domain": "softbank.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/softbank.ai"
  },
  {
    "domain": "monsterbevcorp.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/monsterbevcorp.ai"
  },
  {
    "domain": "chinatelecom-h.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/chinatelecom-h.ai"
  },
  {
    "domain": "licindia.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/licindia.ai"
  },
  {
    "domain": "midea.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/midea.ai"
  },
  {
    "domain": "chanel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/chanel.ai"
  },
  {
    "domain": "angloamerican.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/angloamerican.ai"
  },
  {
    "domain": "oreillyauto.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/oreillyauto.ai"
  },
  {
    "domain": "enterpriseproducts.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/enterpriseproducts.ai"
  },
  {
    "domain": "adm.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/adm.ai"
  },
  {
    "domain": "brookfield.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/brookfield.ai"
  },
  {
    "domain": "vmware.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/vmware.ai"
  },
  {
    "domain": "keurigdrpepper.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/keurigdrpepper.ai"
  },
  {
    "domain": "cib.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cib.ai"
  },
  {
    "domain": "adanienterprises.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/adanienterprises.ai"
  },
  {
    "domain": "moodys.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/moodys.ai"
  },
  {
    "domain": "eni.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/eni.ai"
  },
  {
    "domain": "airbnb.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/airbnb.ai"
  },
  {
    "domain": "shinetsu.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/shinetsu.ai"
  },
  {
    "domain": "bayer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bayer.ai"
  },
  {
    "domain": "dominionenergy.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/dominionenergy.ai"
  },
  {
    "domain": "pernod-ricard.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/pernod-ricard.ai"
  },
  {
    "domain": "recruit-holdings.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/recruit-holdings.ai"
  },
  {
    "domain": "generalmills.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/generalmills.ai"
  },
  {
    "domain": "rb.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/rb.ai"
  },
  {
    "domain": "itcportal.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/itcportal.ai"
  },
  {
    "domain": "nintendo.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/nintendo.ai"
  },
  {
    "domain": "publicstorage.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/publicstorage.ai"
  },
  {
    "domain": "kraftheinzcompany.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/kraftheinzcompany.ai"
  },
  {
    "domain": "lukoil.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/lukoil.ai"
  },
  {
    "domain": "sx-xhcfj.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/sx-xhcfj.ai"
  },
  {
    "domain": "edfenergy.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/edfenergy.ai"
  },
  {
    "domain": "sempra.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/sempra.ai"
  },
  {
    "domain": "santander.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/santander.ai"
  },
  {
    "domain": "aep.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/aep.ai"
  },
  {
    "domain": "uber.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/uber.ai"
  },
  {
    "domain": "phillips66.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/phillips66.ai"
  },
  {
    "domain": "synopsys.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/synopsys.ai"
  },
  {
    "domain": "thehersheycompany.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/thehersheycompany.ai"
  },
  {
    "domain": "hitachi.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/hitachi.ai"
  },
  {
    "domain": "gm.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/gm.ai"
  },
  {
    "domain": "takeda.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/takeda.ai"
  },
  {
    "domain": "valero.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/valero.ai"
  },
  {
    "domain": "lseg.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/lseg.ai"
  },
  {
    "domain": "pacificorp.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/pacificorp.ai"
  },
  {
    "domain": "anz.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/anz.ai"
  },
  {
    "domain": "stc.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/stc.ai"
  },
  {
    "domain": "mitsubishicorp.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/mitsubishicorp.ai"
  },
  {
    "domain": "ir-bri.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/ir-bri.ai"
  },
  {
    "domain": "southerncoppercorp.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/southerncoppercorp.ai"
  },
  {
    "domain": "itau.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/itau.ai"
  },
  {
    "domain": "marriott.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/marriott.ai"
  },
  {
    "domain": "home.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/home.ai"
  },
  {
    "domain": "bajajfinserv.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/bajajfinserv.ai"
  },
  {
    "domain": "hikvision.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/hikvision.ai"
  },
  {
    "domain": "ir.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ir.ai"
  },
  {
    "domain": "lzlj.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/lzlj.ai"
  },
  {
    "domain": "cintas.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cintas.ai"
  },
  {
    "domain": "3ds.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/3ds.ai"
  },
  {
    "domain": "itochu.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/itochu.ai"
  },
  {
    "domain": "kimberly-clark.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/kimberly-clark.ai"
  },
  {
    "domain": "centene.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/centene.ai"
  },
  {
    "domain": "stellantis.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/stellantis.ai"
  },
  {
    "domain": "bankfab.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bankfab.ai"
  },
  {
    "domain": "tel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/tel.ai"
  },
  {
    "domain": "mitsui.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/mitsui.ai"
  },
  {
    "domain": "edwards.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/edwards.ai"
  },
  {
    "domain": "qnb.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/qnb.ai"
  },
  {
    "domain": "bankcomm.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bankcomm.ai"
  },
  {
    "domain": "daikin.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/daikin.ai"
  },
  {
    "domain": "ford.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ford.ai"
  },
  {
    "domain": "woodside.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/woodside.ai"
  },
  {
    "domain": "ropertech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ropertech.ai"
  },
  {
    "domain": "autozone.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/autozone.ai"
  },
  {
    "domain": "foxconn.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/foxconn.ai"
  },
  {
    "domain": "olc.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/olc.ai"
  },
  {
    "domain": "dpdhl.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/dpdhl.ai"
  },
  {
    "domain": "basf.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/basf.ai"
  },
  {
    "domain": "amphenol.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/amphenol.ai"
  },
  {
    "domain": "munichre.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/munichre.ai"
  },
  {
    "domain": "ing.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ing.ai"
  },
  {
    "domain": "samsungbiologics.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/samsungbiologics.ai"
  },
  {
    "domain": "aflac.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/aflac.ai"
  },
  {
    "domain": "nationalgrid.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/nationalgrid.ai"
  },
  {
    "domain": "snowflake.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/snowflake.ai"
  },
  {
    "domain": "fedex.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/fedex.ai"
  },
  {
    "domain": "ikea.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ikea.ai"
  },
  {
    "domain": "travelers.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/travelers.ai"
  },
  {
    "domain": "dsv.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/dsv.ai"
  },
  {
    "domain": "cadence.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cadence.ai"
  },
  {
    "domain": "ambev.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ambev.ai"
  },
  {
    "domain": "agilent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/agilent.ai"
  },
  {
    "domain": "investor.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/investor.ai"
  },
  {
    "domain": "johnsoncontrols.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/johnsoncontrols.ai"
  },
  {
    "domain": "adyen.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/adyen.ai"
  },
  {
    "domain": "en.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/en.ai"
  },
  {
    "domain": "hess.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/hess.ai"
  },
  {
    "domain": "universalmusic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/universalmusic.ai"
  },
  {
    "domain": "macquarie.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/macquarie.ai"
  },
  {
    "domain": "kotak.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/kotak.ai"
  },
  {
    "domain": "tokiomarinehd.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/tokiomarinehd.ai"
  },
  {
    "domain": "dexcom.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/dexcom.ai"
  },
  {
    "domain": "adanigas.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/adanigas.ai"
  },
  {
    "domain": "motorolasolutions.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/motorolasolutions.ai"
  },
  {
    "domain": "shopify.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/shopify.ai"
  },
  {
    "domain": "cbrands.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/cbrands.ai"
  },
  {
    "domain": "exeloncorp.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/exeloncorp.ai"
  },
  {
    "domain": "paloaltonetworks.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/paloaltonetworks.ai"
  },
  {
    "domain": "biontech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/biontech.ai"
  },
  {
    "domain": "biotech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/biotech.ai"
  },
  {
    "domain": "chugai-pharm.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/chugai-pharm.ai"
  },
  {
    "domain": "suncor.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/suncor.ai"
  },
  {
    "domain": "fmgl.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/fmgl.ai"
  },
  {
    "domain": "corteva.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/corteva.ai"
  },
  {
    "domain": "intesasanpaolo.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/intesasanpaolo.ai"
  },
  {
    "domain": "ihsmarkit.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/ihsmarkit.ai"
  },
  {
    "domain": "workday.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/workday.ai"
  },
  {
    "domain": "budweiserapac.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/budweiserapac.ai"
  },
  {
    "domain": "paychex.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/paychex.ai"
  },
  {
    "domain": "maaden.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/maaden.ai"
  },
  {
    "domain": "skhynix.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/skhynix.ai"
  },
  {
    "domain": "republicservices.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/republicservices.ai"
  },
  {
    "domain": "ecolab.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ecolab.ai"
  },
  {
    "domain": "ocbc.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ocbc.ai"
  },
  {
    "domain": "devonenergy.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/devonenergy.ai"
  },
  {
    "domain": "nxp.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/nxp.ai"
  },
  {
    "domain": "compass-group.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/compass-group.ai"
  },
  {
    "domain": "kindermorgan.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/kindermorgan.ai"
  },
  {
    "domain": "tcenergy.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/tcenergy.ai"
  },
  {
    "domain": "autodesk.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/autodesk.ai"
  },
  {
    "domain": "co.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/co.ai"
  },
  {
    "domain": "realtyincome.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/realtyincome.ai"
  },
  {
    "domain": "kkr.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/kkr.ai"
  },
  {
    "domain": "xilinx.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/xilinx.ai"
  },
  {
    "domain": "sf-express.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sf-express.ai"
  },
  {
    "domain": "bce.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bce.ai"
  },
  {
    "domain": "biogen.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/biogen.ai"
  },
  {
    "domain": "edeka.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/edeka.ai"
  },
  {
    "domain": "enphase.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/enphase.ai"
  },
  {
    "domain": "en.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/en.ai"
  },
  {
    "domain": "bayan.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bayan.ai"
  },
  {
    "domain": "citics.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/citics.ai"
  },
  {
    "domain": "rossstores.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/rossstores.ai"
  },
  {
    "domain": "nornickel.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/nornickel.ai"
  },
  {
    "domain": "lululemon.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/lululemon.ai"
  },
  {
    "domain": "ajg.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/ajg.ai"
  },
  {
    "domain": "fisglobal.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/fisglobal.ai"
  },
  {
    "domain": "infineon.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/infineon.ai"
  },
  {
    "domain": "sysco.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sysco.ai"
  },
  {
    "domain": "shkp.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/shkp.ai"
  },
  {
    "domain": "harris.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/harris.ai"
  },
  {
    "domain": "chipotle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/chipotle.ai"
  },
    {
    "domain": "edeka.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/edeka.ai"
  },
  {
    "domain": "enphase.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/enphase.ai"
  },
  {
    "domain": "en.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/en.ai"
  },
  {
    "domain": "bayan.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bayan.ai"
  },
  {
    "domain": "citics.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/citics.ai"
  },
  {
    "domain": "rossstores.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/rossstores.ai"
  },
  {
    "domain": "nornickel.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/nornickel.ai"
  },
  {
    "domain": "lululemon.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/lululemon.ai"
  },
  {
    "domain": "ajg.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/ajg.ai"
  },
  {
    "domain": "fisglobal.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/fisglobal.ai"
  },
  {
    "domain": "infineon.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/infineon.ai"
  },
  {
    "domain": "sysco.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sysco.ai"
  },
  {
    "domain": "shkp.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/shkp.ai"
  },
  {
    "domain": "harris.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/harris.ai"
  },
  {
    "domain": "chipotle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/chipotle.ai"
  },
  {
    "domain": "tranetechnologies.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/tranetechnologies.ai"
  },
  {
    "domain": "larsentoubro.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/larsentoubro.ai"
  },
  {
    "domain": "sands.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sands.ai"
  },
  {
    "domain": "halliburton.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/halliburton.ai"
  },
  {
    "domain": "asianpaints.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/asianpaints.ai"
  },
  {
    "domain": "mizuho-fg.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/mizuho-fg.ai"
  },
  {
    "domain": "lgchem.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/lgchem.ai"
  },
  {
    "domain": "kfh.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/kfh.ai"
  },
  {
    "domain": "chinayanghe.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/chinayanghe.ai"
  },
  {
    "domain": "wesfarmers.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/wesfarmers.ai"
  },
  {
    "domain": "Metaverse.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Metaverse.ai"
  },
  {
    "domain": "NFT.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/NFT.ai"
  },
  {
    "domain": "crypto.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/crypto.ai"
  },
  {
    "domain": "blockchain.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/blockchain.ai"
  },
  {
    "domain": "AI.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/AI.ai"
  },
  {
    "domain": "machine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/machine.ai"
  },
  {
    "domain": "learning.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/learning.ai"
  },
  {
    "domain": "quantum.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/quantum.ai"
  },
  {
    "domain": "computing.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/computing.ai"
  },
  {
    "domain": "AR.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/AR.ai"
  },
  {
    "domain": "VR.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/VR.ai"
  },
  {
    "domain": "XR.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/XR.ai"
  },
  {
    "domain": "neuralink.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/neuralink.ai"
  },
  {
    "domain": "biohacking.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/biohacking.ai"
  },
  {
    "domain": "transhumanism.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/transhumanism.ai"
  },
  {
    "domain": "singularity.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/singularity.ai"
  },
  {
    "domain": "digitization.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/digitization.ai"
  },
  {
    "domain": "automation.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/automation.ai"
  },
  {
    "domain": "robotics.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/robotics.ai"
  },
  {
    "domain": "drones.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/drones.ai"
  },
  {
    "domain": "self-driving.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/self-driving.ai"
  },
  {
    "domain": "IoT.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/IoT.ai"
  },
  {
    "domain": "smart.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/smart.ai"
  },
  {
    "domain": "big.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/big.ai"
  },
  {
    "domain": "data.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/data.ai"
  },
  {
    "domain": "science.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/science.ai"
  },
  {
    "domain": "fintech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/fintech.ai"
  },
  {
    "domain": "insurtech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/insurtech.ai"
  },
  {
    "domain": "proptech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/proptech.ai"
  },
  {
    "domain": "healthtech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/healthtech.ai"
  },
  {
    "domain": "edtech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/edtech.ai"
  },
  {
    "domain": "govtech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/govtech.ai"
  },
  {
    "domain": "legaltech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/legaltech.ai"
  },
  {
    "domain": "martech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/martech.ai"
  },
  {
    "domain": "adtech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/adtech.ai"
  },
  {
    "domain": "greentech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/greentech.ai"
  },
  {
    "domain": "cleantech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cleantech.ai"
  },
  {
    "domain": "nanotech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/nanotech.ai"
  },
  {
    "domain": "biotech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/biotech.ai"
  },
  {
    "domain": "synthethic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/synthethic.ai"
  },
  {
    "domain": "biology.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/biology.ai"
  },
  {
    "domain": "CRISPR.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/CRISPR.ai"
  },
  {
    "domain": "cloud.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cloud.ai"
  },
  {
    "domain": "computing.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/computing.ai"
  },
  {
    "domain": "SaaS.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/SaaS.ai"
  },
  {
    "domain": "PaaS.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/PaaS.ai"
  },
  {
    "domain": "IaaS.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/IaaS.ai"
  },
  {
    "domain": "WiFi.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/WiFi.ai"
  },
  {
    "domain": "streaming.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/streaming.ai"
  },
  {
    "domain": "influencer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/influencer.ai"
  },
  {
    "domain": "social.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/social.ai"
  },
  {
    "domain": "media.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/media.ai"
  },
  {
    "domain": "podcasts.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/podcasts.ai"
  },
  {
    "domain": "vlogging.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/vlogging.ai"
  },
  {
    "domain": "hyperlocal.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/hyperlocal.ai"
  },
  {
    "domain": "gig.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/gig.ai"
  },
  {
    "domain": "economy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/economy.ai"
  },
  {
    "domain": "crowdsourcing.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/crowdsourcing.ai"
  },
  {
    "domain": "sharing.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sharing.ai"
  },
  {
    "domain": "economy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/economy.ai"
  },
  {
    "domain": "subscription.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/subscription.ai"
  },
  {
    "domain": "model.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/model.ai"
  },
  {
    "domain": "B2B.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/B2B.ai"
  },
  {
    "domain": "B2C.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/B2C.ai"
  },
  {
    "domain": "C2C.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/C2C.ai"
  },
  {
    "domain": "on-demand.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/on-demand.ai"
  },
  {
    "domain": "ecommerce.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ecommerce.ai"
  },
  {
    "domain": "mcommerce.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mcommerce.ai"
  },
  {
    "domain": "omnichannel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/omnichannel.ai"
  },
  {
    "domain": "UX.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/UX.ai"
  },
  {
    "domain": "CX.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/CX.ai"
  },
  {
    "domain": "DX.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/DX.ai"
  },
  {
    "domain": "blockchain.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/blockchain.ai"
  },
  {
    "domain": "tokenization.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/tokenization.ai"
  },
  {
    "domain": "decentralization.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/decentralization.ai"
  },
  {
    "domain": "DeFi.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/DeFi.ai"
  },
  {
    "domain": "crypto.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/crypto.ai"
  },
  {
    "domain": "wallet.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/wallet.ai"
  },
  {
    "domain": "stablecoin.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/stablecoin.ai"
  },
  {
    "domain": "bitcoin.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bitcoin.ai"
  },
  {
    "domain": "ethereum.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ethereum.ai"
  },
  {
    "domain": "smart.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/smart.ai"
  },
  {
    "domain": "contract.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/contract.ai"
  },
  {
    "domain": "NFT.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/NFT.ai"
  },
  {
    "domain": "metaverse.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/metaverse.ai"
  },
  {
    "domain": "multiverse.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/multiverse.ai"
  },
  {
    "domain": "digital.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/digital.ai"
  },
  {
    "domain": "twin.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/twin.ai"
  },
  {
    "domain": "extended.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/extended.ai"
  },
  {
    "domain": "reality.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/reality.ai"
  },
  {
    "domain": "virtual.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/virtual.ai"
  },
  {
    "domain": "reality.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/reality.ai"
  },
  {
    "domain": "augmented.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/augmented.ai"
  },
  {
    "domain": "reality.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/reality.ai"
  },
  {
    "domain": "mixed.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mixed.ai"
  },
  {
    "domain": "reality.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/reality.ai"
  },
  {
    "domain": "digital.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/digital.ai"
  },
  {
    "domain": "identity.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/identity.ai"
  },
  {
    "domain": "e-residency.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/e-residency.ai"
  },
  {
    "domain": "digital.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/digital.ai"
  },
  {
    "domain": "nomad.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/nomad.ai"
  },
  {
    "domain": "remote.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/remote.ai"
  },
  {
    "domain": "work.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/work.ai"
  },
  {
    "domain": "workation.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/workation.ai"
  },
  {
    "domain": "bleisure.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/bleisure.ai"
  },
  {
    "domain": "staycation.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/staycation.ai"
  },
  {
    "domain": "athleisure.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/athleisure.ai"
  },
  {
    "domain": "normcore.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/normcore.ai"
  },
  {
    "domain": "hypebeast.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/hypebeast.ai"
  },
  {
    "domain": "sneakerhead.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sneakerhead.ai"
  },
  {
    "domain": "livestream.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/livestream.ai"
  },
  {
    "domain": "dropshipping.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/dropshipping.ai"
  },
  {
    "domain": "viral.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/viral.ai"
  },
  {
    "domain": "meme.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/meme.ai"
  },
  {
    "domain": "cancel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cancel.ai"
  },
  {
    "domain": "culture.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/culture.ai"
  },
  {
    "domain": "performative.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/performative.ai"
  },
  {
    "domain": "activism.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/activism.ai"
  },
  {
    "domain": "virtue.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/virtue.ai"
  },
  {
    "domain": "signaling.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/signaling.ai"
  },
  {
    "domain": "microaggression.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/microaggression.ai"
  },
  {
    "domain": "intersectionality.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/intersectionality.ai"
  },
  {
    "domain": "representation.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/representation.ai"
  },
  {
    "domain": "diversity.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/diversity.ai"
  },
  {
    "domain": "inclusion.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/inclusion.ai"
  },
  {
    "domain": "allyship.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/allyship.ai"
  },
  {
    "domain": "sustainability.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sustainability.ai"
  },
  {
    "domain": "net.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/net.ai"
  },
  {
    "domain": "zero.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/zero.ai"
  },
  {
    "domain": "carbon.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/carbon.ai"
  },
  {
    "domain": "footprint.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/footprint.ai"
  },
  {
    "domain": "upcycling.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/upcycling.ai"
  },
  {
    "domain": "tiny.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/tiny.ai"
  },
  {
    "domain": "home.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/home.ai"
  },
  {
    "domain": "van.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/van.ai"
  },
  {
    "domain": "life.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/life.ai"
  },
  {
    "domain": "digital.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/digital.ai"
  },
  {
    "domain": "detox.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/detox.ai"
  },
  {
    "domain": "forest.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/forest.ai"
  },
  {
    "domain": "bathing.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/bathing.ai"
  },
  {
    "domain": "self-care.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/self-care.ai"
  },
  {
    "domain": "mental.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mental.ai"
  },
  {
    "domain": "health.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/health.ai"
  },
  {
    "domain": "telemedicine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/telemedicine.ai"
  },
  {
    "domain": "telehealth.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/telehealth.ai"
  },
  {
    "domain": "femtech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/femtech.ai"
  },
  {
    "domain": "medtech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/medtech.ai"
  },
  {
    "domain": "e-patient.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/e-patient.ai"
  },
  {
    "domain": "personalized.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/personalized.ai"
  },
  {
    "domain": "medicine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/medicine.ai"
  },
  {
    "domain": "precision.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/precision.ai"
  },
  {
    "domain": "medicine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/medicine.ai"
  },
  {
    "domain": "microbiome.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/microbiome.ai"
  },
  {
    "domain": "mhealth.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mhealth.ai"
  },
  {
    "domain": "wearables.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/wearables.ai"
  },
  {
    "domain": "IoMT.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/IoMT.ai"
  },
  {
    "domain": "digital.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/digital.ai"
  },
  {
    "domain": "therapeutics.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/therapeutics.ai"
  },
  {
    "domain": "biohacking.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/biohacking.ai"
  },
  {
    "domain": "transhumanism.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/transhumanism.ai"
  },
  {
    "domain": "longevity.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/longevity.ai"
  },
  {
    "domain": "bioprinting.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/bioprinting.ai"
  },
  {
    "domain": "cultured.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cultured.ai"
  },
  {
    "domain": "meat.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/meat.ai"
  },
  {
    "domain": "alternative.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/alternative.ai"
  },
  {
    "domain": "protein.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/protein.ai"
  },
  {
    "domain": "cellular.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cellular.ai"
  },
  {
    "domain": "agriculture.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/agriculture.ai"
  },
  {
    "domain": "vertical.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/vertical.ai"
  },
  {
    "domain": "farming.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/farming.ai"
  },
  {
    "domain": "hydroponics.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/hydroponics.ai"
  },
  {
    "domain": "aquaponics.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/aquaponics.ai"
  },
  {
    "domain": "aeroponics.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/aeroponics.ai"
  },
  {
    "domain": "urban.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/urban.ai"
  },
  {
    "domain": "farming.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/farming.ai"
  },
  {
    "domain": "agtech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/agtech.ai"
  },
  {
    "domain": "foodtech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/foodtech.ai"
  },
  {
    "domain": "future.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/future.ai"
  },
  {
    "domain": "food.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/food.ai"
  },
  {
    "domain": "cellular.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cellular.ai"
  },
  {
    "domain": "agriculture.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/agriculture.ai"
  },
  {
    "domain": "alt.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/alt.ai"
  },
  {
    "domain": "protein.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/protein.ai"
  },
  {
    "domain": "plant-based.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/plant-based.ai"
  },
  {
    "domain": "clean.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/clean.ai"
  },
  {
    "domain": "meat.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/meat.ai"
  },
  {
    "domain": "indoor.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/indoor.ai"
  },
  {
    "domain": "farming.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/farming.ai"
  },
  {
    "domain": "robotics.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/robotics.ai"
  },
  {
    "domain": "drones.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/drones.ai"
  },
  {
    "domain": "autonomous.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/autonomous.ai"
  },
  {
    "domain": "vehicles.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/vehicles.ai"
  },
  {
    "domain": "machine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/machine.ai"
  },
  {
    "domain": "learning.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/learning.ai"
  },
  {
    "domain": "deep.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/deep.ai"
  },
  {
    "domain": "learning.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/learning.ai"
  },
  {
    "domain": "neural.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/neural.ai"
  },
  {
    "domain": "networks.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/networks.ai"
  },
  {
    "domain": "natural.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/natural.ai"
  },
  {
    "domain": "language.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/language.ai"
  },
  {
    "domain": "processing.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/processing.ai"
  },
  {
    "domain": "computer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/computer.ai"
  },
  {
    "domain": "vision.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/vision.ai"
  },
  {
    "domain": "edge.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/edge.ai"
  },
  {
    "domain": "computing.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/computing.ai"
  },
  {
    "domain": "WiFi.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/WiFi.ai"
  },
  {
    "domain": "orbital.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/orbital.ai"
  },
  {
    "domain": "computing.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/computing.ai"
  },
  {
    "domain": "space.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/space.ai"
  },
  {
    "domain": "tech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/tech.ai"
  },
  {
    "domain": "spacetech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/spacetech.ai"
  },
  {
    "domain": "NewSpace.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/NewSpace.ai"
  },
  {
    "domain": "space.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/space.ai"
  },
  {
    "domain": "mining.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mining.ai"
  },
  {
    "domain": "off-world.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/off-world.ai"
  },
  {
    "domain": "living.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/living.ai"
  },
  {
    "domain": "microlaunchers.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/microlaunchers.ai"
  },
  {
    "domain": "smallsats.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/smallsats.ai"
  },
  {
    "domain": "cubesats.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/cubesats.ai"
  },
  {
    "domain": "spinners.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/spinners.ai"
  },
  {
    "domain": "hyperloops.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/hyperloops.ai"
  },
  {
    "domain": "evacuated.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/evacuated.ai"
  },
  {
    "domain": "tubes.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/tubes.ai"
  },
  {
    "domain": "maglev.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/maglev.ai"
  },
  {
    "domain": "trains.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/trains.ai"
  },
  {
    "domain": "high-speed.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/high-speed.ai"
  },
  {
    "domain": "rail.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/rail.ai"
  },
  {
    "domain": "vacuum.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/vacuum.ai"
  },
  {
    "domain": "trains.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/trains.ai"
  },
  {
    "domain": "electric.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/electric.ai"
  },
  {
    "domain": "aviation.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/aviation.ai"
  },
  {
    "domain": "eVTOLs.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/eVTOLs.ai"
  },
  {
    "domain": "AAM.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/AAM.ai"
  },
  {
    "domain": "UAM.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/UAM.ai"
  },
  {
    "domain": "flying.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/flying.ai"
  },
  {
    "domain": "cars.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cars.ai"
  },
  {
    "domain": "lidar.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/lidar.ai"
  },
  {
    "domain": "autonomous.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/autonomous.ai"
  },
  {
    "domain": "ships.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ships.ai"
  },
  {
    "domain": "brainiac.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/brainiac.ai"
  },
  {
    "domain": "cognitron.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cognitron.ai"
  },
  {
    "domain": "neuronet.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/neuronet.ai"
  },
  {
    "domain": "synapster.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/synapster.ai"
  },
  {
    "domain": "cortexly.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cortexly.ai"
  },
  {
    "domain": "mentee.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mentee.ai"
  },
  {
    "domain": "intellecto.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/intellecto.ai"
  },
  {
    "domain": "sagemind.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sagemind.ai"
  },
  {
    "domain": "geniuso.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/geniuso.ai"
  },
  {
    "domain": "brightspark.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/brightspark.ai"
  },
  {
    "domain": "ideasprout.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/ideasprout.ai"
  },
  {
    "domain": "envisioneer.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/envisioneer.ai"
  },
  {
    "domain": "futurehub.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/futurehub.ai"
  },
  {
    "domain": "rocketbrain.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/rocketbrain.ai"
  },
  {
    "domain": "bigthink.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bigthink.ai"
  },
  {
    "domain": "cognext.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cognext.ai"
  },
  {
    "domain": "mindspring.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mindspring.ai"
  },
  {
    "domain": "brainstormer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/brainstormer.ai"
  },
  {
    "domain": "ideagenerator.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ideagenerator.ai"
  },
  {
    "domain": "thoughtex.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/thoughtex.ai"
  },
  {
    "domain": "innovatorium.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/innovatorium.ai"
  },
  {
    "domain": "creativitylab.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/creativitylab.ai"
  },
  {
    "domain": "breakthrough.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/breakthrough.ai"
  },
  {
    "domain": "eureka.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/eureka.ai"
  },
  {
    "domain": "visionquest.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/visionquest.ai"
  },
  {
    "domain": "enlighten.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/enlighten.ai"
  },
  {
    "domain": "brainbox.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/brainbox.ai"
  },
  {
    "domain": "mentalex.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/mentalex.ai"
  },
  {
    "domain": "mastermind.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mastermind.ai"
  },
  {
    "domain": "cerebral.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cerebral.ai"
  },
  {
    "domain": "intellect.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/intellect.ai"
  },
  {
    "domain": "cleverbot.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cleverbot.ai"
  },
  {
    "domain": "wiseowl.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/wiseowl.ai"
  },
  {
    "domain": "smartcookie.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/smartcookie.ai"
  },
  {
    "domain": "brainiac.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/brainiac.ai"
  },
  {
    "domain": "brainstorm.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/brainstorm.ai"
  },
  {
    "domain": "mentee.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mentee.ai"
  },
  {
    "domain": "thinktank.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/thinktank.ai"
  },
  {
    "domain": "insights.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/insights.ai"
  },
  {
    "domain": "ideaplus.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/ideaplus.ai"
  },
  {
    "domain": "inspired.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/inspired.ai"
  },
  {
    "domain": "creativemind.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/creativemind.ai"
  },
  {
    "domain": "inventor.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/inventor.ai"
  },
  {
    "domain": "innovate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/innovate.ai"
  },
  {
    "domain": "disrupt.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/disrupt.ai"
  },
  {
    "domain": "transformer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/transformer.ai"
  },
  {
    "domain": "gamechange.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/gamechange.ai"
  },
  {
    "domain": "revolutionize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/revolutionize.ai"
  },
  {
    "domain": "visualize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/visualize.ai"
  },
  {
    "domain": "optimind.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/optimind.ai"
  },
  {
    "domain": "futurevise.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/futurevise.ai"
  },
  {
    "domain": "foresight.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/foresight.ai"
  },
  {
    "domain": "predict.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/predict.ai"
  },
  {
    "domain": "unfold.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/unfold.ai"
  },
  {
    "domain": "unfold.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/unfold.ai"
  },
  {
    "domain": "ion.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ion.ai"
  },
  {
    "domain": "cognify.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cognify.ai"
  },
  {
    "domain": "apti.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/apti.ai"
  },
  {
    "domain": "intelli.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/intelli.ai"
  },
  {
    "domain": "cognitiva.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cognitiva.ai"
  },
  {
    "domain": "mentis.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mentis.ai"
  },
  {
    "domain": "cerebrum.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cerebrum.ai"
  },
  {
    "domain": "cortex.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cortex.ai"
  },
  {
    "domain": "cogniton.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cogniton.ai"
  },
  {
    "domain": "intelect.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/intelect.ai"
  },
  {
    "domain": "mentem.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mentem.ai"
  },
  {
    "domain": "sapien.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sapien.ai"
  },
  {
    "domain": "sapient.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sapient.ai"
  },
  {
    "domain": "mentalis.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/mentalis.ai"
  },
  {
    "domain": "pysch.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/pysch.ai"
  },
  {
    "domain": "Novus.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Novus.ai"
  },
  {
    "domain": "momentum.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/momentum.ai"
  },
  {
    "domain": "acumen.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/acumen.ai"
  },
  {
    "domain": "cognosco.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/cognosco.ai"
  },
  {
    "domain": "perspicax.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/perspicax.ai"
  },
  {
    "domain": "mentem.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mentem.ai"
  },
  {
    "domain": "cognita.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cognita.ai"
  },
  {
    "domain": "comperio.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/comperio.ai"
  },
  {
    "domain": "percipio.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/percipio.ai"
  },
  {
    "domain": "scio.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/scio.ai"
  },
  {
    "domain": "sapio.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sapio.ai"
  },
  {
    "domain": "capio.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/capio.ai"
  },
  {
    "domain": "intellego.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/intellego.ai"
  },
  {
    "domain": "animadverto.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/animadverto.ai"
  },
  {
    "domain": "inspicio.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/inspicio.ai"
  },
  {
    "domain": "Einstein.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/Einstein.ai"
  },
  {
    "domain": "genius.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/genius.ai"
  },
  {
    "domain": "mastermind.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mastermind.ai"
  },
  {
    "domain": "intellect.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/intellect.ai"
  },
  {
    "domain": "expert.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/expert.ai"
  },
  {
    "domain": "guru.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/guru.ai"
  },
  {
    "domain": "prodigy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/prodigy.ai"
  },
  {
    "domain": "savant.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/savant.ai"
  },
  {
    "domain": "brainiac.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/brainiac.ai"
  },
  {
    "domain": "polymath.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/polymath.ai"
  },
  {
    "domain": "innovator.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/innovator.ai"
  },
  {
    "domain": "inventor.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/inventor.ai"
  },
  {
    "domain": "pioneer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/pioneer.ai"
  },
  {
    "domain": "trailblazer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/trailblazer.ai"
  },
  {
    "domain": "visionary.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/visionary.ai"
  },
  {
    "domain": "thoughtleader.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/thoughtleader.ai"
  },
  {
    "domain": "scientist.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/scientist.ai"
  },
  {
    "domain": "creative.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/creative.ai"
  },
  {
    "domain": "brightspark.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/brightspark.ai"
  },
  {
    "domain": "sharpcookie.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/sharpcookie.ai"
  },
  {
    "domain": "rocketscientist.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/rocketscientist.ai"
  },
  {
    "domain": "brainbox.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/brainbox.ai"
  },
  {
    "domain": "egghead.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/egghead.ai"
  },
  {
    "domain": "wiseowl.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/wiseowl.ai"
  },
  {
    "domain": "breakthrough.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/breakthrough.ai"
  },
  {
    "domain": "eureka.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/eureka.ai"
  },
  {
    "domain": "aha.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/aha.ai"
  },
  {
    "domain": "epiphany.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/epiphany.ai"
  },
  {
    "domain": "solution.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/solution.ai"
  },
  {
    "domain": "answer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/answer.ai"
  },
  {
    "domain": "resolve.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/resolve.ai"
  },
  {
    "domain": "solve.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/solve.ai"
  },
  {
    "domain": "unlock.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/unlock.ai"
  },
  {
    "domain": "pioneer.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/pioneer.ai"
  },
  {
    "domain": "transform.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/transform.ai"
  },
  {
    "domain": "reinvent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/reinvent.ai"
  },
  {
    "domain": "change.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/change.ai"
  },
  {
    "domain": "shift.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/shift.ai"
  },
  {
    "domain": "switch.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/switch.ai"
  },
  {
    "domain": "pivot.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/pivot.ai"
  },
  {
    "domain": "alter.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/alter.ai"
  },
  {
    "domain": "modify.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/modify.ai"
  },
  {
    "domain": "evolve.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/evolve.ai"
  },
  {
    "domain": "adapt.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/adapt.ai"
  },
  {
    "domain": "convert.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/convert.ai"
  },
  {
    "domain": "expand.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/expand.ai"
  },
  {
    "domain": "transform.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/transform.ai"
  },
  {
    "domain": "metamorphose.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/metamorphose.ai"
  },
  {
    "domain": "revolutionize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/revolutionize.ai"
  },
  {
    "domain": "disrupt.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/disrupt.ai"
  },
  {
    "domain": "innovate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/innovate.ai"
  },
  {
    "domain": "create.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/create.ai"
  },
  {
    "domain": "reimagine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/reimagine.ai"
  },
  {
    "domain": "rethink.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/rethink.ai"
  },
  {
    "domain": "redefine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/redefine.ai"
  },
  {
    "domain": "restructure.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/restructure.ai"
  },
  {
    "domain": "reshape.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/reshape.ai"
  },
  {
    "domain": "reformulate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/reformulate.ai"
  },
  {
    "domain": "reboot.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/reboot.ai"
  },
  {
    "domain": "refresh.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/refresh.ai"
  },
  {
    "domain": "recreate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/recreate.ai"
  },
  {
    "domain": "reengineer.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/reengineer.ai"
  },
  {
    "domain": "rebuild.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/rebuild.ai"
  },
  {
    "domain": "retool.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/retool.ai"
  },
  {
    "domain": "reinvent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/reinvent.ai"
  },
  {
    "domain": "reinvigorate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/reinvigorate.ai"
  },
  {
    "domain": "reenergize.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/reenergize.ai"
  },
  {
    "domain": "resuscitate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/resuscitate.ai"
  },
  {
    "domain": "revitalize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/revitalize.ai"
  },
  {
    "domain": "reawaken.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/reawaken.ai"
  },
  {
    "domain": "stimulate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/stimulate.ai"
  },
  {
    "domain": "inspire.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/inspire.ai"
  },
  {
    "domain": "energize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/energize.ai"
  },
  {
    "domain": "revamp.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/revamp.ai"
  },
  {
    "domain": "rekindle.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/rekindle.ai"
  },
  {
    "domain": "reignite.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/reignite.ai"
  },
  {
    "domain": "recharge.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/recharge.ai"
  },
  {
    "domain": "refuel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/refuel.ai"
  },
  {
    "domain": "replenish.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/replenish.ai"
  },
  {
    "domain": "restore.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/restore.ai"
  },
  {
    "domain": "resuscitate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/resuscitate.ai"
  },
  {
    "domain": "revive.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/revive.ai"
  },
  {
    "domain": "renew.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/renew.ai"
  },
  {
    "domain": "rejuvenate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/rejuvenate.ai"
  },
  {
    "domain": "regenerate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/regenerate.ai"
  },
  {
    "domain": "reinvigorate.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/reinvigorate.ai"
  },
  {
    "domain": "revitalize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/revitalize.ai"
  },
  {
    "domain": "breathe new life into.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/breathe new life into.ai"
  },
  {
    "domain": "refresh.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/refresh.ai"
  },
  {
    "domain": "reenergize.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/reenergize.ai"
  },
  {
    "domain": "galvanize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/galvanize.ai"
  },
  {
    "domain": "dynamize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/dynamize.ai"
  },
  {
    "domain": "develop.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/develop.ai"
  },
  {
    "domain": "grow.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/grow.ai"
  },
  {
    "domain": "build.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/build.ai"
  },
  {
    "domain": "expand.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/expand.ai"
  },
  {
    "domain": "extend.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/extend.ai"
  },
  {
    "domain": "increase.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/increase.ai"
  },
  {
    "domain": "evolve.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/evolve.ai"
  },
  {
    "domain": "progress.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/progress.ai"
  },
  {
    "domain": "advance.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/advance.ai"
  },
  {
    "domain": "amend.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/amend.ai"
  },
  {
    "domain": "augment.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/augment.ai"
  },
  {
    "domain": "boost.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/boost.ai"
  },
  {
    "domain": "elevate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/elevate.ai"
  },
  {
    "domain": "enhance.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/enhance.ai"
  },
  {
    "domain": "magnify.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/magnify.ai"
  },
  {
    "domain": "optimize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/optimize.ai"
  },
  {
    "domain": "update.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/update.ai"
  },
  {
    "domain": "upgrade.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/upgrade.ai"
  },
  {
    "domain": "amplify.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/amplify.ai"
  },
  {
    "domain": "magnify.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/magnify.ai"
  },
  {
    "domain": "maximize.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/maximize.ai"
  },
  {
    "domain": "raise.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/raise.ai"
  },
  {
    "domain": "heighten.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/heighten.ai"
  },
  {
    "domain": "enrich.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/enrich.ai"
  },
  {
    "domain": "improve.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/improve.ai"
  },
  {
    "domain": "refine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/refine.ai"
  },
  {
    "domain": "cultivate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cultivate.ai"
  },
  {
    "domain": "nurture.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/nurture.ai"
  },
  {
    "domain": "bloom.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bloom.ai"
  },
  {
    "domain": "insightful.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/insightful.ai"
  },
  {
    "domain": "intuitive.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/intuitive.ai"
  },
  {
    "domain": "ingenious.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ingenious.ai"
  },
  {
    "domain": "inventive.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/inventive.ai"
  },
  {
    "domain": "innovative.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/innovative.ai"
  },
  {
    "domain": "imaginative.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/imaginative.ai"
  },
  {
    "domain": "inspired.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/inspired.ai"
  },
  {
    "domain": "visionary.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/visionary.ai"
  },
  {
    "domain": "creative.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/creative.ai"
  },
  {
    "domain": "original.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/original.ai"
  },
  {
    "domain": "novel.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/novel.ai"
  },
  {
    "domain": "avantgarde.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/avantgarde.ai"
  },
  {
    "domain": "cuttingedge.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cuttingedge.ai"
  },
  {
    "domain": "advanced.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/advanced.ai"
  },
  {
    "domain": "progress.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/progress.ai"
  },
  {
    "domain": "futurefacing.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/futurefacing.ai"
  },
  {
    "domain": "nextgen.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/nextgen.ai"
  },
  {
    "domain": "hyperconnected.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/hyperconnected.ai"
  },
  {
    "domain": "accelerated.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/accelerated.ai"
  },
  {
    "domain": "exponential.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/exponential.ai"
  },
  {
    "domain": "abundancedriven.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/abundancedriven.ai"
  },
  {
    "domain": "empowered.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/empowered.ai"
  },
  {
    "domain": "enhanced.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/enhanced.ai"
  },
  {
    "domain": "enriched.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/enriched.ai"
  },
  {
    "domain": "automated.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/automated.ai"
  },
  {
    "domain": "autonomous.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/autonomous.ai"
  },
  {
    "domain": "selfdriving.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/selfdriving.ai"
  },
  {
    "domain": "smart.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/smart.ai"
  },
  {
    "domain": "intelligent.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/intelligent.ai"
  },
  {
    "domain": "cognitive.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cognitive.ai"
  },
  {
    "domain": "sentient.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sentient.ai"
  },
  {
    "domain": "sapient.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/sapient.ai"
  },
  {
    "domain": "conscious.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/conscious.ai"
  },
  {
    "domain": "agile.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/agile.ai"
  },
  {
    "domain": "adaptive.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/adaptive.ai"
  },
  {
    "domain": "responsive.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/responsive.ai"
  },
  {
    "domain": "dynamic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/dynamic.ai"
  },
  {
    "domain": "evolving.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/evolving.ai"
  },
  {
    "domain": "selflearning.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/selflearning.ai"
  },
  {
    "domain": "deeplearning.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/deeplearning.ai"
  },
  {
    "domain": "artificialintelligence.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/artificialintelligence.ai"
  },
  {
    "domain": "machineintelligence.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/machineintelligence.ai"
  },
  {
    "domain": "neuralnetworks.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/neuralnetworks.ai"
  },
  {
    "domain": "naturallanguage.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/naturallanguage.ai"
  },
  {
    "domain": "computervision.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/computervision.ai"
  },
  {
    "domain": "augmentedreality.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/augmentedreality.ai"
  },
  {
    "domain": "virtualreality.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/virtualreality.ai"
  },
  {
    "domain": "mixedreality.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/mixedreality.ai"
  },
  {
    "domain": "extendedreality.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/extendedreality.ai"
  },
  {
    "domain": "enhancedreality.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/enhancedreality.ai"
  },
  {
    "domain": "immersive.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/immersive.ai"
  },
  {
    "domain": "haptics.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/haptics.ai"
  },
  {
    "domain": "multisensory.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/multisensory.ai"
  },
  {
    "domain": "biohacking.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/biohacking.ai"
  },
  {
    "domain": "transhumanism.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/transhumanism.ai"
  },
  {
    "domain": "humanaugmentation.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/humanaugmentation.ai"
  },
  {
    "domain": "humanenhancement.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/humanenhancement.ai"
  },
  {
    "domain": "brainmachine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/brainmachine.ai"
  },
  {
    "domain": "wearables.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/wearables.ai"
  },
  {
    "domain": "implants.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/implants.ai"
  },
  {
    "domain": "exoskeletons.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/exoskeletons.ai"
  },
  {
    "domain": "telepresence.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/telepresence.ai"
  },
  {
    "domain": "telesurgery.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/telesurgery.ai"
  },
  {
    "domain": "remoteexpertise.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/remoteexpertise.ai"
  },
  {
    "domain": "telemedicine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/telemedicine.ai"
  },
  {
    "domain": "digitalhealth.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/digitalhealth.ai"
  },
  {
    "domain": "personalizedmedicine.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/personalizedmedicine.ai"
  },
  {
    "domain": "quantifiedself.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/quantifiedself.ai"
  },
  {
    "domain": "bioprinting.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/bioprinting.ai"
  },
  {
    "domain": "robotic.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/robotic.ai"
  },
  {
    "domain": "cobots.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cobots.ai"
  },
  {
    "domain": "drones.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/drones.ai"
  },
  {
    "domain": "AV.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/AV.ai"
  },
  {
    "domain": "EV.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/EV.ai"
  },
  {
    "domain": "VR.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/VR.ai"
  },
  {
    "domain": "AI.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/AI.ai"
  },
  {
    "domain": "ML.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ML.ai"
  },
  {
    "domain": "bots.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bots.ai"
  },
  {
    "domain": "IoT.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/IoT.ai"
  },
  {
    "domain": "IIoT.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/IIoT.ai"
  },
  {
    "domain": "5G.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/5G.ai"
  },
  {
    "domain": "WiFi6.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/WiFi6.ai"
  },
  {
    "domain": "meshnetworks.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/meshnetworks.ai"
  },
  {
    "domain": "edgecomputing.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/edgecomputing.ai"
  },
  {
    "domain": "blockchain.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/blockchain.ai"
  },
  {
    "domain": "decentralization.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/decentralization.ai"
  },
  {
    "domain": "cryptography.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cryptography.ai"
  },
  {
    "domain": "bitcoin.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/bitcoin.ai"
  },
  {
    "domain": "ethereum.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ethereum.ai"
  },
  {
    "domain": "defi.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/defi.ai"
  },
  {
    "domain": "tokenization.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/tokenization.ai"
  },
  {
    "domain": "smartcontracts.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/smartcontracts.ai"
  },
  {
    "domain": "dapps.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/dapps.ai"
  },
  {
    "domain": "NFTs.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/NFTs.ai"
  },
  {
    "domain": "dao.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/dao.ai"
  },
  {
    "domain": "metaverse.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/metaverse.ai"
  },
  {
    "domain": "spatialcomputing.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/spatialcomputing.ai"
  },
  {
    "domain": "XR.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/XR.ai"
  },
  {
    "domain": "MR.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/MR.ai"
  },
  {
    "domain": "UR.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/UR.ai"
  },
  {
    "domain": "HUD.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/HUD.ai"
  },
  {
    "domain": "AR.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/AR.ai"
  },
  {
    "domain": "VR.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/VR.ai"
  },
  {
    "domain": "QS.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/QS.ai"
  },
  {
    "domain": "disruptive.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/disruptive.ai"
  },
  {
    "domain": "exponential.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/exponential.ai"
  },
  {
    "domain": "innovation.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/innovation.ai"
  },
  {
    "domain": "invention.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/invention.ai"
  },
  {
    "domain": "transformation.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/transformation.ai"
  },
  {
    "domain": "futuretech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/futuretech.ai"
  },
  {
    "domain": "emergingtech.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/emergingtech.ai"
  },
  {
    "domain": "breakthru.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/breakthru.ai"
  },
  {
    "domain": "gamechanger.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/gamechanger.ai"
  },
  {
    "domain": "cuttingedge.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/cuttingedge.ai"
  },
  {
    "domain": "rocketscience.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/rocketscience.ai"
  },
  {
    "domain": "spaceage.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/spaceage.ai"
  },
  {
    "domain": "jetsons.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/jetsons.ai"
  },
  {
    "domain": "tomorrow.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/tomorrow.ai"
  },
  {
    "domain": "beyond.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/beyond.ai"
  },
  {
    "domain": "forward.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/forward.ai"
  },
  {
    "domain": "ahead.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ahead.ai"
  },
  {
    "domain": "nextgeneration.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/nextgeneration.ai"
  },
  {
    "domain": "genius.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/genius.ai"
  },
  {
    "domain": "einstein.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/einstein.ai"
  },
  {
    "domain": "ideas.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/ideas.ai"
  },
  {
    "domain": "brainstorm.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/brainstorm.ai"
  },
  {
    "domain": "brainiac.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/brainiac.ai"
  },
  {
    "domain": "bigthinker.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/bigthinker.ai"
  },
  {
    "domain": "visionary.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/visionary.ai"
  },
  {
    "domain": "prodigy.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/prodigy.ai"
  },
  {
    "domain": "whizkid.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/whizkid.ai"
  },
  {
    "domain": "maverick.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/maverick.ai"
  },
  {
    "domain": "phenom.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/phenom.ai"
  },
  {
    "domain": "flashofbrilliance.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/flashofbrilliance.ai"
  },
  {
    "domain": "eureka.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/eureka.ai"
  },
  {
    "domain": "lightbulb.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/lightbulb.ai"
  },
  {
    "domain": "brightspark.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/brightspark.ai"
  },
  {
    "domain": "firestarter.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/firestarter.ai"
  },
  {
    "domain": "kindlemind.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/kindlemind.ai"
  },
  {
    "domain": "igniteideas.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/igniteideas.ai"
  },
  {
    "domain": "sparkwonders.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/sparkwonders.ai"
  },
  {
    "domain": "blazetrails.ai",
    "available": true,
    "purchaseLink": "https://oneword.domains/d/blazetrails.ai"
  },
  {
    "domain": "enlighten.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/enlighten.ai"
  },
  {
    "domain": "illuminate.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/illuminate.ai"
  },
  {
    "domain": "inspire.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/inspire.ai"
  },
  {
    "domain": "awakening.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/awakening.ai"
  },
  {
    "domain": "realization.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/realization.ai"
  },
  {
    "domain": "envision.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/envision.ai"
  },
  {
    "domain": "breakthrough.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/breakthrough.ai"
  },
  {
    "domain": "epiphany.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/epiphany.ai"
  },
  {
    "domain": "imaginarium.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/imaginarium.ai"
  },
  {
    "domain": "futureworld.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/futureworld.ai"
  },
  {
    "domain": "innovation.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/innovation.ai"
  },
  {
    "domain": "moonshot.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/moonshot.ai"
  },
  {
    "domain": "groundbreaker.ai",
    "available": false,
    "purchaseLink": "https://oneword.domains/d/groundbreaker.ai"
  }
]

# Filter out the available domains 
available_domains = [d for d in domains if d['available']]
print(available_domains)

# Write the available domains to a CSV file 
with open('available_domains.csv', 'a', newline='') as csvfile: 
    fieldnames = ['domain', 'available', 'purchaseLink'] 
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader() 
    for domain in available_domains: 
        writer.writerow(domain)
