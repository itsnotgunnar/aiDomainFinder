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
  }
]

# Filter out the available domains 
available_domains = [d for d in domains if d['available']] 
# Write the available domains to a CSV file 
with open('available_domains.csv', 'a', newline='') as csvfile: 
    fieldnames = ['domain', 'available', 'purchaseLink'] 
    writer = csv.DictWriter(csvfile)
    writer.writeheader() 
    for domain in available_domains: 
        writer.writerow(domain)
